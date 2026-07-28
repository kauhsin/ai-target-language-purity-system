import importlib.util
from pathlib import Path
P=Path(__file__).parents[1]/"src/char_ngram_baseline.py"; S=importlib.util.spec_from_file_location("b",P); b=importlib.util.module_from_spec(S); S.loader.exec_module(b)
def test_grams_and_toy_fit():
    assert "阿拉" in b.grams("阿拉")
    rows=[{"text":"阿拉侃","label":"Shanghainese","id":"1"},{"text":"我哋佢","label":"Cantonese","id":"2"},{"text":"我们他","label":"Mandarin","id":"3"}]
    m=b.fit(rows)
    assert b.predict(m,"阿拉侃")=="Shanghainese"
