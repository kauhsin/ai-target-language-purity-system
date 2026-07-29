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

The balanced corpus assembly and source-level screening required to begin
data-split design are complete. This is not a claim that every sentence has
received final human review. Detailed QA will continue in small, checkpointed
batches throughout later development.

The current corpus snapshot is the input to Milestone 2 design. When
accumulated QA produces a new dataset version, that version must be recorded
before later split implementation or experiments.

## Transition to Milestone 2

The next active milestone is **Milestone 2: Data-Split Design**. Discuss and
design only:

- train/validation/test ratios;
- grouping and leakage-prevention rules;
- cross-language overlap handling;
- source, length, and register stratification checks;
- reproducibility and QA-version interaction.

Stop before implementation and wait for explicit approval. Milestone 3
challenge-set design, Milestone 4 baseline work, Transformer training,
explanation/occlusion work, UI development, and later milestones remain out of
scope.
