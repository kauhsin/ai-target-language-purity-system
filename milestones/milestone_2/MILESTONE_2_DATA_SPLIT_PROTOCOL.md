# Milestone 2: Data-Split Protocol

Status: Frozen implementation completed 2026-08-04. The hard-group,
split-ratio, sealed-test, QA-version stability, reproducibility, and validation
principles below describe the frozen split version
`m2_split_frozen_2026-08-04_v1`.

## Scope

Milestone 2 designs, implements, validates, and freezes the reproducible
train/validation/test split for the three target-language reference corpora.
Challenge-set design and baseline modeling are later milestones.

## Approved Hard-Group Policy

Splitting uses the smallest reliable dependency unit available from upstream
metadata. Known dependencies are atomic: every record in one final group must
enter train, validation, or test together.

The approved public-safe rules are:

- group records by reliable speaker, conversation, transcript, document,
  lesson, scene, template, or other explicit upstream unit when available;
- namespace upstream group identifiers by source before combining them;
- keep exact normalized duplicates in one group and apply the approved
  within-language deduplication rule before final splitting;
- keep exact normalized cross-language overlaps in one shared overlap group;
- keep orthographic, script-conversion, and correction variants together when
  multiple versions enter an experiment;
- introduce `parallel_group_id` only when parallel material is explicitly
  admitted; it is not active for the primary reference corpus;
- treat a record as a singleton group when no reliable dependency metadata or
  detected hard relationship exists;
- merge overlapping hard relationships transitively into one final dependency
  group;
- preserve hard-group integrity even when doing so prevents an exact target
  split percentage.

Concrete source identities, private paths, source-specific recovery rules,
group counts, and exceptional group assignments remain in the private
canonical architecture and private data records.

## Approved Split Target

The target is approximately:

- 80% train;
- 10% validation;
- 10% sealed reference test.

This is a project-specific tradeoff rather than a universal standard. It keeps
most low-resource examples available for training while leaving enough
independent groups for model selection and final evaluation. Hard-group
integrity takes priority over exact percentages.

Validation may guide development decisions. The sealed reference test must not
guide cleaning, threshold selection, feature design, model selection, or
checkpoint selection after the split is frozen.

## Approved Duplicate and Similarity Boundary

Confirmed duplicates and repeated template families are cleaning issues, not
only grouping issues. A template family has substantially the same sentence
skeleton and changes only a location, person, number, or another slot. Keeping
every variant in one split prevents leakage but does not prevent training skew,
so repeated families must be reduced before splitting.

For example, these rows share one explicit location-slot template:

```text
I got lost in Location A.
I got lost in Location B.
I got lost in Location C.
```

Likewise, minor politeness or sentence-final-particle variants of the same
question may be one near-template family.

Semantic or topical similarity alone is not a hard dependency. Two sentences
may both describe going out on the weekend while using different structures
and having no shared source or derivation. Such rows are not automatically
deduplicated or grouped.

Similarity thresholds are candidate-retrieval settings, not universal
standards. A new soft-similarity category must be reviewed with examples before
it becomes a deletion or grouping rule.

## Approved QA-Version Stability

For a later QA release, unchanged groups should retain their previous split
whenever practical. Existing groups move only when a new dependency creates a
conflict or the retained assignment becomes materially invalid. Every move
must be recorded.

Exact reruns of one frozen version require stable record ordering, a fixed
random seed, versioned grouping and splitting rules, and input/output hashes.

## Implemented Milestone 2 Decisions

- The approved hierarchical allocation priority is language totals, then
  source, then register, then length.
- Source/register/length are reported quantitatively without arbitrary automatic
  failure thresholds; hard integrity checks remain failure gates.
- The deterministic group-aware allocator uses stable ordering, a fixed seed,
  and fixed search parameters.
- The manifest records input, rule, allocator, assignment, output, validation,
  status, and version-lineage hashes.
- The frozen validation suite checks group integrity, forced placement, source
  coverage, language totals, leakage, output consistency, and independent
  assignment reproducibility.
- The frozen split is 12,495 train / 1,563 validation / 1,563 sealed test,
  with 4,165 / 521 / 521 records per language.
