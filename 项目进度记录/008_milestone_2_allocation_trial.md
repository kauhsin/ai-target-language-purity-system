# Milestone 2 Allocation Trial

Date: 2026-08-04

## Outcome

Milestone 2 completed a trial-only, group-aware allocation experiment. The
frozen reference corpus was read only; no train/validation/test split was
frozen and no manifest was created.

The experiment enforced complete dependency groups, the approved fixed-train
large group, and complete-group representation from every source in every
split. It compared hierarchical priorities for source, register, and length
balance after language totals.

## Reproducible trial method

A deterministic multi-start search used a stable ordering, a fixed seed,
fixed search counts, and group-preserving moves/swaps. Two independent runs
produced byte-identical assignment and report outputs. Source-specific data,
private paths, and record-level assignments remain private.

Each language achieved 4,165 train, 521 validation, and 521 sealed-reference
test records, which is the closest integer realization of the approved
approximately 80/10/10 target.

The priority-consistent trial candidate produced the best source balance among
the tested reproducible candidates, while alternatives illustrated the expected
trade-offs when register or length balance is promoted. This is evidence for
the upcoming allocation review, not a split freeze.

## Next Milestone 2 work

Review the trial candidate and tolerance/reporting policy; then implement the
manifest, validation suite, actual allocation, and version freeze. Milestone 3
challenge-set design and later work remain out of scope.
