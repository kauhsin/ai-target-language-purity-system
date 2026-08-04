# Milestone 2: Frozen Split Closure

Date: 2026-08-04

Milestone 2 — data-split design, implementation, validation, and freeze — is
complete for the first reproducible split version. The frozen three-language
reference corpus contains 15,621 records in total.

## Frozen result

- Target ratio: approximately 80% train / 10% validation / 10% sealed test.
- Train: 12,495 records.
- Validation: 1,563 records.
- Sealed test: 1,563 records.
- Per language: 4,165 train / 521 validation / 521 sealed-test records.
- Split version: `m2_split_frozen_2026-08-04_v1`.

The approved hard-group rules remain primary. The fixed large Shanghainese
group remains in train, every source is represented in every split, and no
normalized text leakage occurs across splits.

## Reproducibility and validation

The selected deterministic allocator was run twice independently and produced
the same assignment. The final validation passed group integrity, forced-group
placement, source coverage, language totals, leakage checks, materialized-file
consistency, and independent assignment reproducibility.

Exact file hashes and the machine-readable manifest are retained in the
private repository. The sealed test is now frozen and must not guide later
cleaning, feature, threshold, model, or checkpoint decisions.

## Boundary

Milestone 3 challenge-set design and later baseline/model work are not part of
this closure and require a separate explicit start.
