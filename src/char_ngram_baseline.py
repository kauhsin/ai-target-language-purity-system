#!/usr/bin/env python3
"""Dependency-light character n-gram Multinomial Naive Bayes baseline."""
import argparse, json, math
from collections import Counter, defaultdict
from pathlib import Path

LABELS=("Shanghainese","Cantonese","Mandarin")
def grams(text,a=2,b=5):
    text=f"^{text}$"
    return Counter(text[i:i+n] for n in range(a,b+1) for i in range(len(text)-n+1))
def read(path): return [json.loads(x) for x in Path(path).read_text(encoding="utf-8").splitlines() if x]
def fit(rows,alpha=.5):
    counts={l:Counter() for l in LABELS}; totals=Counter(); docs=Counter(r["label"] for r in rows); vocab=set()
    for r in rows:
        g=grams(r["text"]); counts[r["label"]].update(g); totals[r["label"]]+=sum(g.values()); vocab.update(g)
    return counts,totals,docs,len(vocab),alpha
def predict(model,text):
    counts,totals,docs,v,alpha=model; g=grams(text); n=sum(docs.values()); scores={}
    for l in LABELS:
        scores[l]=math.log(docs[l]/n)+sum(c*(math.log(counts[l][x]+alpha)-math.log(totals[l]+alpha*v)) for x,c in g.items())
    return max(scores,key=scores.get)
def evaluate(model,rows):
    cm={a:{p:0 for p in LABELS} for a in LABELS}; errors=[]
    for r in rows:
        p=predict(model,r["text"]); cm[r["label"]][p]+=1
        if p!=r["label"]: errors.append({"id":r["id"],"text":r["text"],"actual":r["label"],"predicted":p})
    per={}
    for l in LABELS:
        tp=cm[l][l]; support=sum(cm[l].values()); pred=sum(cm[a][l] for a in LABELS)
        pr=tp/pred if pred else 0; rc=tp/support if support else 0
        per[l]={"precision":pr,"recall":rc,"f1":2*pr*rc/(pr+rc) if pr+rc else 0,"support":support}
    return {"accuracy":sum(cm[l][l] for l in LABELS)/len(rows),"macro_f1":sum(per[l]["f1"] for l in LABELS)/3,"per_language":per,"confusion_matrix":cm,"error_count":len(errors),"errors":errors}
def main():
    p=argparse.ArgumentParser(); p.add_argument("--data-dir",required=True); p.add_argument("--output",required=True); a=p.parse_args()
    d=Path(a.data_dir); model=fit(read(d/"train.jsonl")); result={s:evaluate(model,read(d/f"{s}.jsonl")) for s in ("validation","test")}
    Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps({s:{k:v for k,v in x.items() if k!="errors"} for s,x in result.items()},ensure_ascii=False,indent=2))
if __name__=="__main__": main()
