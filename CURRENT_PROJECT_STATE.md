# Current Project State

Last updated: 2026-07-29

## Project

**AI Target Language Purity System**

The project builds an explainable system for analyzing whether human-written or
AI-generated text matches its intended language. The initial target languages
are Shanghainese, Cantonese, and Mandarin.

In this project, *purity* describes that match. It does not imply that languages
themselves are pure or should be isolated from outside influence.

## Current Phase and Milestone

The project is in **Phase 1 — AI Target Language Purity Engine**.

**Milestone 0: Problem Definition and Output Protocol is complete.**

**Milestone 1: Dataset Engineering is complete for provisional v1.** The first
balanced snapshot is frozen with input hashes, deterministic grouped splits,
overlap checks, and corpus statistics.

**Milestone 2: Rule-based / N-gram Baseline is complete for provisional v1.**

No Transformer or production model has been implemented. Detailed corpus QA
continues in small versioned batches and does not block development. Every new
QA data release must rebuild the statistics, overlap groups, grouped split,
and baseline before results are compared.

## Milestone 0 Results

Milestone 0 established:

- a plain-language and formal definition of target-language purity;
- Version 1 scope and explicit non-goals;
- a required runtime input of `target_language` and `text`;
- three-way language scores and a sentence-level assessment;
- automatic word-span evidence using deletion and mask occlusion;
- conservative warning and abstention principles;
- reference-data admission, governance, balance, normalization, deduplication,
  and split principles;
- separate evaluation for target-specific, shared, mixed, orthographic, short,
  and segmentation cases;
- high-level Version 1 success criteria.

The approved specification is
[Milestone 0: Problem Definition and Output Protocol](milestones/milestone_0/MILESTONE_0_PROBLEM_DEFINITION_AND_OUTPUT_PROTOCOL.md).
The detailed reasoning and accepted working decisions remain in
[the Milestone 0 decision log](项目进度记录/004_milestone_0_working_decisions.md).

## Accepted Version 1 Direction

- Use one three-way Transformer classifier for Shanghainese, Cantonese, and
  Mandarin.
- Train on human-produced or credibly human-reviewed target-language reference
  corpora.
- Do not add a `Mixed` class, a second mixed-language detector, or token-level
  language labels.
- Treat language scores as relative model support, not percentages of language
  composition.
- Use deletion and mask occlusion to show how words affect all three scores.
- Prioritize stable negative target-language evidence when locating a possible
  mismatch.
- Do not treat occlusion as independent linguistic proof.
- Preserve shared expressions that are valid in more than one target language
  and evaluate them separately.
- Keep rewriting, automatic correction, open language comparison without a
  target, complex UI, and agent-like behavior outside Version 1.

## Data Direction for Milestone 1

- Start with Shanghainese; its usable data determines the initial corpus
  profile and class size.
- Match Cantonese and Mandarin as closely as practical in quantity, register,
  source type, length, and time period.
- Begin with equal class sizes and nested learning-curve experiments.
- Preserve immutable raw data, then create cleaned and selected layers.
- Record provenance, usage rights, transformations, privacy risks, and source
  concentration.
- Normalize confirmed orthographic variants conservatively; unknown forms are
  not automatically variants.
- Normalize and group duplicates before the final split.
- Deduplicate exact normalized sentences within each language. Keep identical
  cross-language sentences once per language, link them as one overlap group,
  and place them in the same split.
- Apply comparable cleaning and grouping rules across all three languages.

## Milestone 1 Progress

Milestone 1 has established a local, private source-review workflow that
preserves raw materials, records provenance and rights, separates screening
from detailed correction, and marks duplicate relationships before any final
split. Source identities, source-derived records, local data paths, prompts,
and operational notes are maintained only in the private project repository.

The Shanghainese, Cantonese, and Mandarin included working sets are now
assembled at the same class size of 5,209 sentences each. Each language uses
multiple complementary registers, and rejected candidate sources are not
treated as training data. The current totals can be frozen as a reproducible
provisional version for baseline development while detailed QA continues in
small, versioned batches.

This is an initial Milestone 1 closure rather than a claim that every sentence
has completed final human review. The current snapshot is suitable for the
first reproducible baseline; ongoing QA remains part of dataset maintenance.

## Provisional v1 Freeze and Milestone 2 Results

The snapshot contains 15,627 records: 5,209 per language. Each class has 4,167
train, 521 validation, and 521 test records. Exact normalized overlaps and
available upstream groups are atomic within one split. No cross-language exact
normalized overlap was found. One within-Shanghainese normalized duplicate
group remains; both records share one split and are flagged for later QA.

The character 2–5 gram Multinomial Naive Bayes baseline achieved 97.89%
validation accuracy and 97.63% test accuracy. Test macro-F1 was 97.62%. Test
F1 was 96.42% for Shanghainese, 99.14% for Cantonese, and 97.29% for Mandarin.
Of 37 test errors, 36 were Shanghainese predicted as Cantonese or Mandarin.
This asymmetry and class-level length differences make leakage, register,
length, and source-style audits a priority before treating the score as
linguistic validity. Misclassified test records averaged 14.49 characters,
compared with 19.23 for correct predictions.

Naive Bayes was used because scikit-learn was unavailable and installation did
not complete. Same-split TF-IDF logistic regression remains a useful later
replication, but does not block this reproducible baseline.

## Deferred Until Development Evidence Exists

- numerical warning and evidence thresholds;
- calibration methods;
- final sentence-status names and public wording;
- any combined deletion/mask score;
- exact metric pass thresholds;
- final normalization, number-handling, segmentation, and metadata schemas.

These are planned development decisions, not unfinished Milestone 0 scope.

## Next Session

1. Continue small-batch QA without blocking development.
2. When QA accumulates into a named data version, regenerate the freeze,
   statistics, overlaps, grouped split, and baseline.
3. Review provisional v1 before approving another milestone.
4. Do not begin Transformer, explanation, or UI work without new approval.

## Working Rules

For every milestone:

1. discuss;
2. design;
3. obtain explicit approval;
4. implement only the approved scope;
5. review and stop before advancing.

Public-facing core introductions should have natural English and Chinese
versions. Public technical material must have an English version. Internal
engineering records may use whichever language is most practical.

## Repository

GitHub: `https://github.com/kauhsin/ai-target-language-purity-system`
Branch: `main`
