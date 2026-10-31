# Learning Progress

## Current State

- Started: 2026-10-22 (Europe/Warsaw).
- Phase: theoretical introduction.
- Active unit: M00 — Goal And Starting Point.
- Status: parts 1–7 conceptual reviews complete within their recorded scope.
  Part 7 recognizes independent scope-control reasoning and hypothesis/evidence
  reasoning; the ratio setup was mentor-supplied, with no independent numerical
  percentage answer claimed. M00 remains incomplete.
- Latest review: 2026-10-31 (Europe/Warsaw).
- The owner explicitly requested guided learning under the current plan.
- No previous progress record existed; lectures and exercises contained only
  `.gitkeep` placeholders. No completed preparation is evidenced in this repository.
  The learner has not reported preparation completed elsewhere; no earlier
  completion is inferred. The current diagnostic and understanding checks now
  provide evidence for continuing M00.

## Context And Delivery

- Sequence, prerequisites, and learning acceptance: [LEARNING.md](../project-guidance/LEARNING.md).
- Analytical scope and product acceptance: [PROJECT.md](../project-guidance/PROJECT.md).
- Starting-point diagnostic: [m00-starting-point.md](exercises/m00-starting-point.md).
- Diagnostic review: [m00-starting-point-feedback.md](exercises/m00-starting-point-feedback.md).
- First lecture part: [m00-01-responsibilities-and-interfaces.md](lectures/m00-01-responsibilities-and-interfaces.md).
- Part 1 understanding review: [m00-01-understanding-feedback.md](exercises/m00-01-understanding-feedback.md).
- Second lecture part: [m00-02-data-meaning-and-contracts.md](lectures/m00-02-data-meaning-and-contracts.md).
- Part 2 understanding review: [m00-02-understanding-feedback.md](exercises/m00-02-understanding-feedback.md).
- Third lecture part: [m00-03-provenance-snapshots-and-reproducibility.md](lectures/m00-03-provenance-snapshots-and-reproducibility.md).
- Part 3 understanding review: [m00-03-understanding-feedback.md](exercises/m00-03-understanding-feedback.md).
- Fourth lecture part: [m00-04-environment-configuration-and-notebook-state.md](lectures/m00-04-environment-configuration-and-notebook-state.md).
- Part 4 understanding review: [m00-04-understanding-feedback.md](exercises/m00-04-understanding-feedback.md).
- Fifth lecture part: [m00-05-pandas-inspection-filtering-and-grouping.md](lectures/m00-05-pandas-inspection-filtering-and-grouping.md).
- Part 5 understanding review: [m00-05-understanding-feedback.md](exercises/m00-05-understanding-feedback.md).
- Sixth lecture part: [m00-06-joins-and-cardinality.md](lectures/m00-06-joins-and-cardinality.md).
- Part 6 understanding review: [m00-06-understanding-feedback.md](exercises/m00-06-understanding-feedback.md).
- Seventh lecture part: [m00-07-charts-and-interpretation.md](lectures/m00-07-charts-and-interpretation.md).
- Part 7 understanding review: [m00-07-understanding-feedback.md](exercises/m00-07-understanding-feedback.md).
- Conversation: Polish. New saved documents/materials: English under
  [AGENTS.md](../AGENTS.md); no repository-specific language override recorded.
- Scope orientation in chat: compare conventional/electric cycle imports and
  exports in Poland, Germany, and the Netherlands for 2017–2025; produce a
  reproducible analysis and report. Trade does not establish retail demand.
- Observed starting skills: correct accumulator trace and Python return result;
  correct SQL grouping/sum and expected values; knows `git status`, needs
  instruction on inspecting changed lines. Broader skills remain unassessed.

## Evidence And Checks

- Inspected current repository instructions, learning guide, project specification,
  maintenance rules, and materials directories.
- Git working tree was clean before starting learning artifacts.
- Learner independently answered the diagnostic in chat: Python result 135 with
  a correct loop trace; SQL `SUM` grouped by room, A = 90 and B = 45; `git status`
  identified, uncertainty about changed-line inspection stated explicitly.
- Feedback distinguishes implicit `None` returns from useful effects and
  identifies `total` as an accumulator. Git diff commands introduced; learner
  use and retention have not been verified. No code or command execution was
  reported by the learner.
- Lecture part 1 covers responsibilities, input/output, validation, calculation,
  reporting, orchestration, functions/modules, interfaces including units, and
  return values versus effects using the fictional reservation example.
  Learner correctly explained that changing the input source preserves downstream
  code when the interface stays stable; he correctly assigned negative-duration
  rejection to validation and required stopping with an informative error.
  Both part 1 conceptual checks are met; implementation is not assessed.
- Lecture part 2 covers grain, simple/composite keys, duplicate detection, units
  and normalization, comparable aggregation/double counting, missing versus zero,
  schema versus data contract, and data-dependent validation/failure policies.
  It explicitly distinguishes positive reservation durations from nonnegative
  daily totals and unknown daily delivery. Learner correctly rejected room-only
  deduplication, identified the expected reservation ID key, and rejected an
  exact complete total with missing daily data. He independently derived the
  valid lower bound of 90 minutes under the example's assumptions.
- Part 2 refinements: learner described grain as room plus duration, assumed
  uniqueness enforcement, and suggested mean/mode imputation with more data.
  Feedback clarifies one reservation per row, attributes versus identifiers,
  actual constraints versus expected keys/CSV/combined data, and why sample
  size alone cannot justify imputation. Supplemental explanations are saved in
  the part 2 lecture. In the follow-up the learner correctly identified one
  reservation per row and no duplicates for distinct IDs with matching room and
  duration. He correctly distinguished estimated values from actual observations
  recovered from another system. Grain/estimation checks are met; uniqueness
  enforcement was explained but not independently re-demonstrated.
- Part 2 terminology refinement: recurring time patterns define seasonality;
  ordinary differences between days do not establish it. Missingness associated
  with busy days need not be seasonal. Source recovery also requires matching
  definitions, units, scope, keys, and relevant revisions.
- Lecture part 3 covers provenance, source corrections, immutable snapshots,
  acquisition versus local processing, manifests, checksums and their limits,
  and reproducing numerical results with specified data/code/config/environment.
  On 2026-10-29 the learner correctly proposed comparing the two snapshots and
  recognized that losing the earlier snapshot prevents direct comparison.
  He correctly declined to guarantee reproduction. For question 2 he later
  clarified that he had overlooked the sentence saying only the corrected
  export remained available; on noticing it, he correctly recognized that the
  original input could not be recovered from that revised export alone.
  Record this as an overlooked condition, not a demonstrated conceptual gap.
  Part 3 conceptual checks are met based on his initial snapshot reasoning and
  clarification. The near-duplicate follow-up is withdrawn following that
  clarification; no answer is pending. The general caveat about unchanged code and
  other run conditions remains in the lecture. All examples remain fictional.
- Teaching adjustment requested by the learner: distinguish missed question
  conditions from conceptual misunderstandings; consider his clarification and
  demonstrated reasoning before assigning another check. The learner further
  clarified that the original assessment was correct for his initial answer:
  the mentor could not have known about the overlooked sentence. The later
  explanation supplies the cause and resolves the check; it does not invalidate
  the original assessment. The feedback records this distinction.
- Lecture part 4 covers interpreter selection, libraries/dependencies/imports,
  virtual environments and activation limits, version specifications and
  indirect dependencies, configuration/Git ignore boundaries, notebook cells
  and kernels, stale/hidden state, fresh-kernel versus fresh-environment checks,
  and modules' limits. Learner correctly identified interpreter mismatch as
  likely, explained why reinstalling in the terminal may not help, traced the
  stale `total` to skipping cell 2, and proposed restarting and running all
  cells in order. Both conceptual checks are met. Clarified that the kernel
  retains the value and that selecting the intended prepared environment is
  an alternative to installing into the current notebook environment.
  No environment was set up, packages installed, versions selected, or notebook
  executed; all examples are instructional.
- Lecture part 5 covers DataFrame/Series, index versus business key, inspection,
  missingness and duplicate-key diagnostics, boolean filtering/column selection,
  and grouping with SQL analogies. On 2026-10-31 the learner correctly derived
  A = 60 and B = 45, identified reservations 2 and 3 as contributors, and
  explained aggregation even with one retained row per group. His explanation
  establishes subset scope; feedback explicitly labels the result grain as one
  room for reservations lasting at least 45 minutes on the sample day. The check
  is met. Accept his explicit conversational shorthand "the code returns" for
  assigning results; it is not evidence of a return/display misunderstanding.
  Official pandas documentation was consulted; examples were manually reasoned,
  not executed. No project dependencies or data were changed.
- Lecture part 6 covers joins and input/output grains, key matching cardinality,
  row multiplication, many-to-one validation, match coverage indicators,
  left versus inner joins, and preservation checks for lookup enrichment.
  Learner correctly derived four rows and 180 minutes for a lookup containing
  B twice, identified the repeated B reservation, and predicted rejection by
  many-to-one validation. Clarified "exactly one match": validation checks
  right-side key uniqueness, while match coverage is separate and zero matches
  can pass the uniqueness check. The part 6 checks are met with that note.
  Examples remain fictional and unexecuted; no packages were installed.
- Lecture part 7 covers bar/line chart purpose, pandas plotting code, axis units
  and zero baselines for bars, scope/coverage, totals versus available-time
  percentages, and observations versus causal hypotheses. Learner asked what
  "available" meant in question 1. The mentor clarified the total bookable window
  but also supplied the specific numerator/denominator substitutions, exceeding
  the requested clarification. The learner correctly objected that this supplied
  part of the solution. The learner subsequently explained that the chat prompt's
  "same day" did not establish a sufficiently explicit link to the earlier
  reservation totals for him. He independently checked business meaning and
  time scope before calculating. Record that as positive analytical evidence,
  not a percentage-calculation failure. The supplied setup remains mentor
  assistance; no independent numerical percentage answer is claimed.
  For question 2 he correctly identified the equipment explanation as a hypothesis,
  proposed surveying users' booking reasons, and offered coffee proximity as an
  alternative. Clarified that survey reports do not alone prove causality,
  empirical hypotheses may remain unresolved, and multiple causes can coexist.
  Part 7 introductory conceptual review is complete with these evidence limits;
  do not repeat arithmetic merely to recognize the demonstrated reasoning.
  A separate conversation illustration is stored in
  `project-materials/lectures/visuals/reserved-minutes.html`; it is not evidence
  of a pandas run or learner execution. Plotting documentation was consulted;
  no environment setup or package installation was performed.
  Local material links and whitespace were checked. The illustration script was
  reviewed statically; it was not browser-rendered and no runtime check is claimed.
- Remaining M00 coverage includes typing/runtime validation,
  exceptions/logging/network boundaries, test levels/fixtures/fakes,
  clean-environment reproduction in practice, and automated quality tools.
  No full M00 pass is recorded.
- Prior preparation elsewhere has not been reported. No independent-exercise
  readiness, source access, data analysis, or project implementation is evidenced.
- The diagnostic prompt and this record were prepared by the agent; they are not
  evidence of learner competence or completion of M00.

## Next Action

Continue M00 with type annotations versus runtime validation. Part 7 review is
closed at the introductory scope without requiring repeated arithmetic; its
independent reasoning and mentor assistance are distinguished in the feedback.
Future prompts must identify relevant data, time scope, grain, and definitions
explicitly. Treat justified business-context clarification as analytical evidence.
For requests to clarify a prompt, explain only the ambiguous term or assumption;
leave value selection, concrete substitutions, and calculations to the learner
unless asked.
Address actual gaps or clarifications without assuming that a missed condition
proves a conceptual misunderstanding. Use the fictional reservation example
for the next theoretical explanation.
Record demonstrated understanding separately from delivered explanations.
Finish all M00 coverage and its acceptance before M01 exercises; main-project
work remains blocked until M01 and M02 readiness is demonstrated.
