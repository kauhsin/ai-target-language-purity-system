# Milestone 4 Baseline Design Checkpoint

Date: 2026-08-08

## Outcome

The teaching and design checkpoint for Phase 1 — Milestone 4 is complete. All
35 baseline decision items are approved. No baseline has been implemented or
trained, and implementation remains gated on the exact owner authorization:

`APPROVED: IMPLEMENT MILESTONE 4`

## Public-safe design summary

- Use a character n-gram sparse-text baseline with a small, predeclared set of
  representation candidates and two standard L2-regularized linear classifier
  families.
- Use the frozen train split only for fitting, and use the frozen validation
  split for the staged, bounded model-selection protocol. Do not retrain on
  train+validation during Milestone 4.
- Emphasize validation Macro F1 while reporting Accuracy, per-class metrics,
  raw and normalized confusion matrices, and sample denominators.
- Preserve all candidate results, audit linear feature reliance, review every
  selected-baseline validation error, and use a transparent evidence-refined
  error taxonomy.
- Record configuration, dependency versions, seeds, convergence, input/output
  SHA-256 lineage, reproduction evidence, and one compact immutable baseline
  package without unnecessary duplicate files.
- Public-safe aggregate evaluation may be published after review; record-level
  and source-revealing artifacts remain private.

## Stop boundary

The sealed reference test and Milestone 3 challenge data must not enter
training or tuning. Do not begin Transformer training, detector evaluation or
calibration, explanation, retrieval, UI, or Phase 2.
