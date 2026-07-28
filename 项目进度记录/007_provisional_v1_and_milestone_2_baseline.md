# Provisional v1 Freeze and Milestone 2 Baseline

Date: 2026-07-29

## Outcome

Milestone 1 is frozen as reproducible `provisional_v1`, and the first
Milestone 2 character n-gram baseline is complete. The snapshot has 15,627
records, with 5,209 records for each language.

The deterministic split uses seed `20260729`. Each language has 4,167 train,
521 validation, and 521 test records. Exact normalized text overlaps and all
available upstream groups remain within one split. Input SHA-256 hashes are
recorded privately. Concrete paths, source identities, source distributions,
and source-derived artifacts remain private.

## Duplicate and leakage checks

No exact normalized sentence occurs across languages. One normalized duplicate
group occurs within the Shanghainese input. Both records were retained to
preserve the approved 5,209-row snapshot, assigned to the same split, and
flagged for later QA.

Mandarin supplied upstream group identifiers, merged with normalized overlap
groups before splitting. The Shanghainese and Cantonese aggregate interfaces
do not supply comparable document, speaker, or dialogue group identifiers.
The split prevents known exact/group leakage but cannot prove that all
near-duplicate or source-context leakage is absent.

## Baseline design

The deterministic baseline uses character 2–5 grams and Multinomial Naive
Bayes with additive smoothing. TF-IDF logistic regression was preferred, but
scikit-learn was unavailable and installation did not complete in the approved
environment. Same-split logistic regression remains a useful later replication.

## Results

| Split | Accuracy | Macro-F1 |
| --- | ---: | ---: |
| Validation | 97.89% | 97.88% |
| Test | 97.63% | 97.62% |

| Test language | Precision | Recall | F1 | Support |
| --- | ---: | ---: | ---: | ---: |
| Shanghainese | 100.00% | 93.09% | 96.42% | 521 |
| Cantonese | 98.48% | 99.81% | 99.14% | 521 |
| Mandarin | 94.73% | 100.00% | 97.29% | 521 |

Test confusion matrix (rows actual, columns predicted):

| Actual / predicted | Shanghainese | Cantonese | Mandarin |
| --- | ---: | ---: | ---: |
| Shanghainese | 485 | 8 | 28 |
| Cantonese | 0 | 520 | 1 |
| Mandarin | 0 | 0 | 521 |

## Initial error analysis

Errors are asymmetric: 36 of 37 test errors are Shanghainese predicted as a
competing language. Initial hypotheses are shared written forms, fewer
high-specificity sequences in some sentences, and corpus differences in
length, register, or source style. These are hypotheses, not linguistic
conclusions. The high score may partly reflect corpus construction.
Misclassified test sentences averaged 14.49 characters, versus 19.23 for
correctly classified test sentences, so short inputs are a concrete early
error factor rather than only a general concern.

QA should prioritize the within-language duplicate, short/shared-form
Shanghainese errors, near-duplicate checks, and stronger group metadata for
aggregates without document or speaker identifiers.

Each accumulated QA release must create a new data version and rerun
normalization, overlap checks, grouped splitting, statistics, baseline,
metrics, confusion matrix, and error analysis.

Milestone 2 stops here for review. Transformer, explanation, and UI work have
not started.
