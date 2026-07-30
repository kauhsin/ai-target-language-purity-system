# Milestone 1 Final Completion

Date: 2026-07-30

## Outcome

Phase 1 Milestone 1 is complete. The frozen reference corpus contains 5,207
sentences for each target language:

- Shanghainese: 5,207;
- Cantonese: 5,207;
- Mandarin: 5,207;
- total: 15,621.

Concrete source identities, source-derived artifacts, local paths, rights
evidence, and operational screening rules remain in the private repository.

## Final validation

The final read-only audit found:

- no blank effective texts;
- unique record IDs within each language;
- no normalized exact duplicate groups within a language;
- no normalized exact overlap groups across languages;
- no unresolved high-similarity candidates under the recorded audit rules.

Similarity thresholds used during cleaning were exploratory candidate-finding
settings, not universal standards. Human review determined which candidates
were true duplicates or repeated templates.

## Template and similarity decisions

Repeated template families must be reduced during data cleaning. Placing every
near-identical slot-filled variant into one split prevents leakage but does not
prevent the repeated structure from skewing training.

Semantic or topical similarity alone does not justify automatic deletion or a
hard dependency group. A hard relationship requires evidence such as a shared
speaker, conversation, document, source group, template, duplicate,
derivation, or parallel relationship.

## Transition to Milestone 2

The next active milestone is **Milestone 2: Data-Split Design,
Implementation, Validation, and Freeze**.

Already approved:

- an approximate 80/10/10 train/validation/sealed-test target;
- the public hard-group policy;
- hard-group integrity over exact percentages;
- a sealed reference test;
- stable split assignments for unchanged groups across small QA releases when
  practical;
- reproducible reruns using stable ordering, a fixed seed, versioned rules,
  and hashes.

Milestone 2 must finish the remaining stratification, allocation algorithm,
tolerance, manifest, validation, implementation, and freeze work.

Stop before Milestone 3 challenge-set design, Milestone 4 baseline work,
Transformer training, explanation work, retrieval, or UI.
