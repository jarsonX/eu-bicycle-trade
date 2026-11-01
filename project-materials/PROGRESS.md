# Learning Progress

## Current State

- Started: 2026-10-22 (Europe/Warsaw).
- Phase: theoretical introduction.
- Active unit: M00 — Goal And Starting Point.
- Status: M00 theory and introductory conceptual review complete. All 11 parts
  were delivered and reviewed within their recorded scope; part 11 feedback
  was saved after discussion, learner clarifications, and his explicit request.
  Active unit remains M00, awaiting his separate confirmation to start M01.
  Part 7's ratio setup remains mentor-supplied, with no independent numerical
  percentage answer claimed. Completion does not imply practical implementation
  mastery or readiness for main-project work.
- Latest delivery: 2026-11-01 (Europe/Warsaw).
- The owner explicitly requested guided learning under the current plan.
- Owner transition boundary: M01 must not start without his explicit
  confirmation. Completing M00 does not grant that confirmation. Keep the
  active unit at M00 after its final review until permission to advance arrives.
- No previous progress record existed; lectures and exercises contained only
  `.gitkeep` placeholders. No completed preparation is evidenced in this repository.
  The learner has not reported preparation completed elsewhere; no earlier
  completion is inferred. The subsequent diagnostic, lectures, discussion, and
  understanding reviews provide the evidence for the completed M00 introduction.

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
- Eighth lecture part: [m00-08-type-hints-and-runtime-validation.md](lectures/m00-08-type-hints-and-runtime-validation.md).
- Part 8 understanding review: [m00-08-understanding-feedback.md](exercises/m00-08-understanding-feedback.md).
- Ninth lecture part: [m00-09-errors-logging-and-network-boundaries.md](lectures/m00-09-errors-logging-and-network-boundaries.md).
- Part 9 understanding review: [m00-09-understanding-feedback.md](exercises/m00-09-understanding-feedback.md).
- Tenth lecture part: [m00-10-testing-and-independent-expectations.md](lectures/m00-10-testing-and-independent-expectations.md).
- Part 10 understanding review: [m00-10-understanding-feedback.md](exercises/m00-10-understanding-feedback.md).
- Eleventh lecture part: [m00-11-quality-gates-and-reproducibility.md](lectures/m00-11-quality-gates-and-reproducibility.md).
- Part 11 understanding review: [m00-11-understanding-feedback.md](exercises/m00-11-understanding-feedback.md).
- Working delivery split stated in chat: 11 M00 lecture parts in total; part 8
  covers types/validation, part 9 exceptions/warnings/logging/network limits,
  part 10 testing, and part 11 quality tools/automation, reproducibility, README,
  and the final M00 understanding review. This subdivision does not change the
  module prerequisites or acceptance in the learning guide.
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
- Lecture part 8 covers value types, argument/return annotations, static
  checking and its limits, plain Python runtime behavior, business constraints
  and units beyond simple types, a bounded nonblank-room-label value check,
  and validation at input boundaries. Learner correctly identified the `int`
  versus `str` return mismatch and lack of plain-Python runtime enforcement;
  he correctly explained integer hour/minute compatibility and normalization
  to the required minutes. Both checks are met. He correctly noted that source
  units and the target contract were already given, so no additional fact
  needed to be established for that question. The mentor's request to
  "establish" more was redundant; no hidden requirements are assessed.
  Python/mypy documentation was consulted; code was reasoned through, not run.
  No type checker, interpreter, dependency, or project component was installed
  or selected. Exceptions are introduced only as needed for the value check;
  handling and failure policy remain in part 9.
- Lecture part 9 covers contract-based failure/warning policy, exceptions and
  selective try/except handling, re-raising, failure status and success artifacts,
  logging levels/configuration and their separation from control flow, source
  acquisition boundaries, response validation, timeout semantics, and bounded
  retries. Learner correctly traced the final print and rejected an empty-table
  success result as masking failure and misleading later analyses. He proposed
  detailed diagnostic logs and distinguished the known timeout symptom from
  possible causes. He also addressed how the analytical team could support users
  when data is irrecoverable, using clear unavailable-data and affected-calculation
  labels. This business proposal was compatible with stopping the invalid run;
  he did not propose that the program autonomously change its contract.
  The mentor's earlier assessment conflated these responsibilities and understated
  his explicit diagnostic reasoning. The feedback now records the correction
  after discussing his explanation. General control-flow and network-timeout
  details were supplementary context, not grounds to misrepresent the answer.
  Part 9 introductory conceptual review is complete; no repeated questions are
  needed. No actual root cause was established in the hypothetical. Official
  Python/Requests documentation was consulted; no examples were run, source data
  fetched, or dependencies selected or installed.
- Feedback workflow clarified by the learner: discuss disputed interpretations
  and doubts in chat before finalizing written feedback. Evaluate business or
  technical extensions on their actual meaning and assumptions. Do not attribute
  automatic program decisions to a proposal about team action, or treat a broader
  reasoned answer as wrong merely because it exceeds the expected answer.
- Lecture part 10 covers automated assertions, unit/integration scope,
  independently derived expectations, normal/edge/error cases, expected
  exceptions, pytest fixtures, temporary test paths, transport doubles,
  regression prevention, isolation/repeatability, and limits of passed tests.
  Learner proposed focused reader-component tests under explicit architectural
  assumptions, reordered equivalent records to distinguish position from values,
  and stage-by-stage integration diagnosis followed by targeted regression tests.
  He correctly replaced source behavior while retaining real coordinator handling
  and proposed immediate success, timeout-then-success, and two-timeout scenarios.
  Discussion added independent expected checks, scoped passing-test claims,
  faithful exception behavior, and explicit attempt counts. He accepted the
  discussion and explicitly requested saving the feedback. Part 10 is complete;
  no implementation or execution is inferred from this conceptual design.
  Official
  pytest documentation was consulted; code examples were reasoned through,
  not executed. No tests, packages, source calls, or project components were run
  or installed, and no learner readiness is inferred from the prepared lecture.
- Lecture part 11 covers Ruff lint versus format, type-check/test/validation
  roles, quality-gate scope, real CI evidence for the evaluated version,
  fresh-environment and exact-snapshot reproduction, verified README handover,
  and the approved project question/scope/product evidence. Learner correctly
  identified the missing actual CI run for B, limits of local checks, the
  undeclared dependency, and the need for the exact historical snapshot. His
  statement about missing data validation referred to missing evidence; the
  mentor's speculation about an unmentioned mechanism was an unnecessary
  correction. He clarified that "sales" meant imports/exports, so no retail/trade
  confusion is inferred. Project interpretation limits, reproducible setup
  repair, and preserving accepted report conclusions were explained during
  discussion, rather than claimed as independently listed beforehand.
  Practical refresh priorities are Python syntax/functions and modular code
  design, learned through practical work without an extra preliminary refresher
  course. Part 11 feedback was saved only after discussion and his explicit
  request. The cumulative introductory M00 review is complete at this level.
  Official tool documentation and current project scope were consulted; no
  Ruff/type-checker/pytest run or CI execution, environment setup, dependency
  selection, source-data acquisition, or M01 work was performed.
- All planned M00 lecture parts and the introductory final review are complete.
  Independent reasoning and mentor assistance remain distinguished in the
  feedback. No implementation, practical readiness, or final-product acceptance
  is claimed. M01 requires the owner's separate explicit confirmation, which
  has not been given; the request to save feedback does not authorize advancing.
- Prior preparation elsewhere has not been reported. No independent-exercise
  readiness, source access, data analysis, or project implementation is evidenced.
- The diagnostic prompt and this record were prepared by the agent; they are not
  evidence of learner competence or completion of M00.

## Next Action

Remain in completed M00 and wait for explicit owner confirmation before M01;
do not start exercise setup, install dependencies, or silently advance units.
The final review and feedback are recorded; do not repeat completed questions.
When the owner confirms moving to M01, read its prerequisites and guide the
independent exercise setup, supporting Python syntax/functions and modularity
as needed. Do not add a separate preliminary Python refresher course.
Assess only stated requirements; do not ask the learner to infer extra unknowns
when the question already supplies the source and contract facts.
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
