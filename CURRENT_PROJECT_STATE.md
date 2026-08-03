# Current Project State

Last updated: 2026-07-30

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

**Milestone 1: Dataset Engineering is complete.** The first frozen,
balanced three-language reference sets have passed final read-only QA and are
ready for the reproducible split.

The project is transitioning to:

```text
Milestone 2: Data-Split Design, Implementation, Validation, and Freeze
```

No production model has been implemented.

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

The Shanghainese, Cantonese, and Mandarin reference sets are frozen at 5,207
sentences per language, or 15,621 sentences in total. Each language uses
multiple complementary registers, and rejected candidate sources are not
treated as training data.

The final read-only audit found no normalized exact duplicate groups within a
language, no normalized exact overlaps across languages, and no unresolved
high-similarity candidates under the recorded audit rules. Future QA remains
possible, but every change must produce a new version and preserve unchanged
group assignments whenever practical.

Similarity thresholds used to find review candidates were exploratory rather
than universal standards. Confirmed duplicate and template decisions were
made through human review and recorded execution trails. Repeated templates
must be reduced during cleaning; broad semantic similarity alone is not enough
to create a hard dependency group.

## Deferred Until Development Evidence Exists

- numerical warning and evidence thresholds;
- calibration methods;
- final sentence-status names and public wording;
- any combined deletion/mask score;
- exact metric pass thresholds;
- final normalization, number-handling, segmentation, and metadata schemas.

These are planned development decisions, not unfinished Milestone 0 scope.

## Deferred Public Showcase Preparation

During active development, maintain sensitive artifacts only in the private
repository and naturally public-safe milestone outputs in the public
repository. Do not create or synchronize public demonstration copies solely
for possible future presentation.

A public-safe toy dataset, runnable demonstration pipeline, example
configuration, and sanitized result package are deferred until the project
owner explicitly decides to prepare the project for public presentation. They
are not an automatic post-QA task and are outside Milestone 2.

## Next Session

Continue Milestone 2 from its approved decisions:

1. use an approximate 80/10/10 train/validation/sealed-test target;
2. retain the completed grouping and deterministic allocation trial as
   non-frozen evidence;
3. review the candidate and tolerance/reporting decision;
4. define the reproducibility manifest and complete validation suite;
5. only then materialize, validate, and freeze the reproducible split.

Milestone 3 challenge-set design and Milestone 4 baseline work remain out of
scope.

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
