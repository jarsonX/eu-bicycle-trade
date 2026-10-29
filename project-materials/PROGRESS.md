# Learning Progress

## Current State

- Started: 2026-10-22 (Europe/Warsaw).
- Phase: theoretical introduction.
- Active unit: M00 — Goal And Starting Point.
- Status: parts 1–4 conceptual checks met within the recorded scope. Part 5
  delivered in chat; its filtering/grouping understanding check awaits a learner
  response. M00 remains incomplete.
- Latest review: 2026-10-29 (Europe/Warsaw).
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
  and grouping with SQL analogies. Its subset-total/grain check awaits a learner
  response. Official pandas documentation was consulted; examples were manually
  reasoned, not executed. No project dependencies or data were changed.
- Remaining M00 coverage includes pandas joins/charts,
  typing/runtime validation,
  exceptions/logging/network boundaries, test levels/fixtures/fakes,
  clean-environment reproduction in practice, and automated quality tools.
  No full M00 pass is recorded.
- Prior preparation elsewhere has not been reported. No independent-exercise
  readiness, source access, data analysis, or project implementation is evidenced.
- The diagnostic prompt and this record were prepared by the agent; they are not
  evidence of learner competence or completion of M00.

## Next Action

Review the part 5 filtering/grouping result, result grain, and subset versus
all-reservations interpretation. Address actual gaps or clarifications without
assuming that a missed condition proves a conceptual misunderstanding. Then
continue M00 with joins, cardinality, and basic chart interpretation using the
fictional reservation example.
Record demonstrated understanding separately from delivered explanations.
Finish all M00 coverage and its acceptance before M01 exercises; main-project
work remains blocked until M01 and M02 readiness is demonstrated.
