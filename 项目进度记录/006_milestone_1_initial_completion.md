# Milestone 1 Initial Provisional Completion

Date: 2026-07-29

## Outcome

Milestone 1 has reached initial provisional completion. The first included
working sets for Shanghainese, Cantonese, and Mandarin contain 5,209 sentences
per language. Each class combines multiple complementary registers rather than
relying on a single source style.

Concrete source identities, local paths, source-derived worksheets, rights
evidence, screening rules, and operational prompts remain in the private
repository. Rejected candidate sources are not treated as training data.

## Meaning of provisional completion

The balanced corpus assembly and source-level screening required to start a
baseline are complete. This is not a claim that every sentence has received
final human review. Detailed QA will continue in small, checkpointed batches
throughout later development.

The current corpus snapshot will be versioned and frozen before the first
baseline. When accumulated QA produces a new dataset version, the affected
statistics, overlap groups, split, and baseline must be regenerated.

## Transition to Milestone 2

The next active milestone is **Milestone 2: Rule-based / N-gram Baseline**.
Prepare the reproducible grouped data snapshot and leakage-safe split, then
implement only:

- a character n-gram baseline;
- baseline metrics;
- initial error analysis.

Transformer training, explanation/occlusion work, UI development, and later
milestones remain out of scope until the baseline is reviewed.
