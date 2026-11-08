# Learning Progress

## Current State

- Started: 2026-10-22 (Europe/Warsaw).
- Phase: independent exercises.
- Active unit: none — M01 complete; M02 is next and has not started.
- Status: M01 completed on 2026-11-08 after starting on 2026-11-07.
  Learner-supplied terminal output confirms
  Python 3.15.2 responds to both `py --version` and `py -V:3.15 --version`.
  Python 3.14 is absent according to the explicit version-selection error.
  Python 3.15 was accepted for the exercise. The learner supplied `Python 3.15.2` from
  `.\.venv\Scripts\python.exe --version` in the assigned exercise directory;
  direct environment-interpreter execution is verified from his output.
  His editor is Visual Studio Code. His earlier `sys.executable` output from
  the terminal resolves to the assigned exercise's `.venv/Scripts/python.exe`.
  The terminal-interpreter and Git ignore/tracking checks are complete within
  their stated scope. Learner-supplied output confirms pytest 9.2.0 installation
  and startup, and an optional pip update from 26.2.2 to 26.3. Recording the
  actual dependency inventory and exercise setup notes is complete as an
  assisted documentation step: the learner created `requirements-dev.txt`,
  and the mentor wrote `SETUP.md` at his explicit request. The requirements
  match his installation log; the later fresh-environment check is recorded below.
  The learner has applied the discussed generator/TypedDict reference, placing
  the type before the data and annotating the list as `list[Reservation]`.
  Mentor checks confirm the disclosed cases and unchanged inputs. The learner
  has protected the example print with an import guard and written three pytest
  tests. His supplied run and mentor verification both report `3 passed in 0.01s`.
  The revised tests have local annotated inputs and no manual module-scope calls;
  mentor verification again reports `3 passed in 0.01s`. Code review is accepted
  for the disclosed three cases. Manual expected-value reasoning has not yet
  been supplied explicitly; its role was explained during review.
  Minimal pytest configuration is complete as an assisted step: the learner
  created the explained reference configuration at his request, and supplied
  output selecting `pytest.ini`, collecting three tests, and passing all three
  without explicit test-path or compact-output arguments. The guided workspace
  Git review is complete: the learner supplied status/diff output, explained
  file selection and the patch after instruction, and created the two scoped
  ignore rules. Follow-up status omits caches and the unwanted sandbox while
  retaining the six intended files. At the learner's request, operational
  documentation now includes example/test execution and expected results;
  the mentor verified both commands in the existing environment.
  Fresh-environment reproduction succeeded in `.venv-repro`: the learner
  supplied creation and baseline evidence, successful pinned installations,
  a freeze matching all 31 requirements, example output `50`, and `3 passed`.
  Mentor verification confirms pip 26.3 under `.venv-repro`. Technical checks
  and the final learner explanation of explicit interpreter selection meet
  M01 acceptance. File-selection reasoning is also demonstrated. M02 readiness
  for main-project work has not yet been established.
  Argument/return annotations remain required.
  M00 theory and introductory
  conceptual review are complete. All 11 parts
  were delivered and reviewed within their recorded scope; part 11 feedback
  was saved after discussion, learner clarifications, and his explicit request.
  Part 7's ratio setup remains mentor-supplied, with no independent numerical
  percentage answer claimed. Completion does not imply practical implementation
  mastery or readiness for main-project work.
- Latest delivery: 2026-11-08 (Europe/Warsaw), final interpreter-selection
  explanation accepted and M01 closed. M02 has not started.
- The owner explicitly requested guided learning under the current plan.
- Owner transition boundary satisfied on 2026-11-07: the learner explicitly
  said "Skończyliśmy M00. Przejdźmy do M01." He reaffirmed that the agent is
  a coach/mentor who teaches problem solving and coding rather than completing
  tasks for him. The learner owns setup, code, tests, and their execution;
  the mentor provides explanations, disclosed tasks, gradual hints, and review.
- No previous progress record existed; lectures and exercises contained only
  `.gitkeep` placeholders. No completed preparation is evidenced in this repository.
  The learner has not reported preparation completed elsewhere; no earlier
  completion is inferred. The subsequent diagnostic, lectures, discussion, and
  understanding reviews provide the evidence for the completed M00 introduction.

## Context And Delivery

- Sequence, prerequisites, and learning acceptance: [LEARNING.md](../project-guidance/LEARNING.md).
- Analytical scope and product acceptance: [PROJECT.md](../project-guidance/PROJECT.md).
- Shared command reference: [COMMANDS.md](COMMANDS.md).
- Exercise setup notes: [SETUP.md](exercises/workspaces/m01-reservations/SETUP.md).
- First M01 task: [m01-01-interpreter-discovery.md](exercises/tasks/m01-01-interpreter-discovery.md).
- Environment creation task: [m01-02-virtual-environment.md](exercises/tasks/m01-02-virtual-environment.md).
- Terminal interpreter task: [m01-03-vscode-interpreter.md](exercises/tasks/m01-03-vscode-interpreter.md).
- Git ignore task: [m01-04-git-ignore.md](exercises/tasks/m01-04-git-ignore.md).
- Pytest installation task: [m01-05-pytest-installation.md](exercises/tasks/m01-05-pytest-installation.md).
- Dependency/setup task: [m01-06-dependencies-and-setup-notes.md](exercises/tasks/m01-06-dependencies-and-setup-notes.md).
- First function task: [m01-07-first-function.md](exercises/tasks/m01-07-first-function.md).
- First test task: [m01-08-first-tests.md](exercises/tasks/m01-08-first-tests.md).
- Pytest configuration task: [m01-09-pytest-configuration.md](exercises/tasks/m01-09-pytest-configuration.md).
- Git review task: [m01-10-git-review.md](exercises/tasks/m01-10-git-review.md).
- Latest completed M01 task: [m01-11-environment-reproduction.md](exercises/tasks/m01-11-environment-reproduction.md).
- Function syntax support: [m01-01-function-syntax-and-type-annotations.md](lectures/m01-01-function-syntax-and-type-annotations.md).
- Starting-point diagnostic: [m00-starting-point.md](exercises/tasks/m00-starting-point.md).
- Diagnostic review: [m00-starting-point-feedback.md](exercises/feedback/m00-starting-point-feedback.md).
- First lecture part: [m00-01-responsibilities-and-interfaces.md](lectures/m00-01-responsibilities-and-interfaces.md).
- Part 1 understanding review: [m00-01-understanding-feedback.md](exercises/feedback/m00-01-understanding-feedback.md).
- Second lecture part: [m00-02-data-meaning-and-contracts.md](lectures/m00-02-data-meaning-and-contracts.md).
- Part 2 understanding review: [m00-02-understanding-feedback.md](exercises/feedback/m00-02-understanding-feedback.md).
- Third lecture part: [m00-03-provenance-snapshots-and-reproducibility.md](lectures/m00-03-provenance-snapshots-and-reproducibility.md).
- Part 3 understanding review: [m00-03-understanding-feedback.md](exercises/feedback/m00-03-understanding-feedback.md).
- Fourth lecture part: [m00-04-environment-configuration-and-notebook-state.md](lectures/m00-04-environment-configuration-and-notebook-state.md).
- Part 4 understanding review: [m00-04-understanding-feedback.md](exercises/feedback/m00-04-understanding-feedback.md).
- Fifth lecture part: [m00-05-pandas-inspection-filtering-and-grouping.md](lectures/m00-05-pandas-inspection-filtering-and-grouping.md).
- Part 5 understanding review: [m00-05-understanding-feedback.md](exercises/feedback/m00-05-understanding-feedback.md).
- Sixth lecture part: [m00-06-joins-and-cardinality.md](lectures/m00-06-joins-and-cardinality.md).
- Part 6 understanding review: [m00-06-understanding-feedback.md](exercises/feedback/m00-06-understanding-feedback.md).
- Seventh lecture part: [m00-07-charts-and-interpretation.md](lectures/m00-07-charts-and-interpretation.md).
- Part 7 understanding review: [m00-07-understanding-feedback.md](exercises/feedback/m00-07-understanding-feedback.md).
- Eighth lecture part: [m00-08-type-hints-and-runtime-validation.md](lectures/m00-08-type-hints-and-runtime-validation.md).
- Part 8 understanding review: [m00-08-understanding-feedback.md](exercises/feedback/m00-08-understanding-feedback.md).
- Ninth lecture part: [m00-09-errors-logging-and-network-boundaries.md](lectures/m00-09-errors-logging-and-network-boundaries.md).
- Part 9 understanding review: [m00-09-understanding-feedback.md](exercises/feedback/m00-09-understanding-feedback.md).
- Tenth lecture part: [m00-10-testing-and-independent-expectations.md](lectures/m00-10-testing-and-independent-expectations.md).
- Part 10 understanding review: [m00-10-understanding-feedback.md](exercises/feedback/m00-10-understanding-feedback.md).
- Eleventh lecture part: [m00-11-quality-gates-and-reproducibility.md](lectures/m00-11-quality-gates-and-reproducibility.md).
- Part 11 understanding review: [m00-11-understanding-feedback.md](exercises/feedback/m00-11-understanding-feedback.md).
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
  is claimed. At the close of M00, separate confirmation for M01 was still
  pending; saving feedback did not authorize advancing. The owner subsequently
  provided that confirmation on 2026-11-07, as recorded in Current State.
- Prior preparation elsewhere has not been reported. No independent-exercise
  readiness, source access, data analysis, or project implementation is evidenced.
- The diagnostic prompt and this record were prepared by the agent; they are not
  evidence of learner competence or completion of M00.
- On 2026-11-07 the mentor re-read repository instructions, the learning guide,
  and the full progress record; M00 completion meets the M01 prerequisite.
  The working tree was clean before this transition. No root `.gitignore`,
  Python dependency/configuration file, or prior M01 task was found in the
  inspected inventory. Interpreter discovery and its explanation were assigned
  in chat and saved in the first M01 prompt. At that point no learner output
  had been received, and no interpreter invocation, environment creation,
  installation, code/test implementation, or learner execution was claimed.
  The mentor did not run the
  discovery task on the learner's behalf. File checks are material maintenance,
  not practical learning evidence.
- The learner subsequently stated that Python is not installed, so command
  output is not required to establish the starting point. The original discovery
  request is withdrawn, not failed. The mentor checked official Python Windows
  installation documentation and release listings, then provided a guided
  installation task using Python install manager and proposed Python 3.14 for
  the exercise. This is an exercise recommendation, not an agreed final project
  runtime or verified dependency stack. At that point installation and version
  verification remained unreported; no installation was performed by the agent.
- The learner then supplied terminal output showing Python 3.15.2 for both
  `py --version` and `py -V:3.15 --version`, and no matching 3.14 runtime.
  Interpreter availability is established by this learner-supplied evidence;
  the installation steps themselves were not observed. The mentor accepts 3.15
  for the M01 exercise, replacing the earlier 3.14 recommendation. Current
  pytest maintainer metadata explicitly lists Python 3.15 support. This is
  declared support, not a local pytest installation or passing test run, and
  does not establish compatibility of the entire future project stack.
  Virtual-environment creation and verification were assigned with explained
  command scaffolding; at that point results were pending. The mentor
  created only the prompt, not the exercise folder, environment, code, or tests.
- Before creating `m01-reservations`, the learner requested organizing the
  exercise directory so practical work would not mix with feedback files.
  The mentor separated existing files into `exercises/tasks/` and
  `exercises/feedback/`, moved the empty-directory placeholder to
  `exercises/workspaces/`, rebased local links, and updated the assigned M01
  path to `project-materials/exercises/workspaces/m01-reservations/`.
  The layout rule is owned by [AGENTS.md](../AGENTS.md). Feedback wording,
  exercise IDs, and recorded learning evidence are preserved; this is repository
  maintenance by the mentor, not learner coding evidence. The practical workspace
  and virtual environment remain uncreated by the mentor.
- The owner explicitly chose `tasks/` for task descriptions. The mentor renamed
  the directory, updated layout guidance and incoming links, and preserved task
  contents. M01 remains active with the same pending learner environment setup.
  Checks: all three moved files have identical SHA256 hashes; 90 local file
  links and 136 Markdown heading anchors resolve; no old directory references
  remain, and `git diff --check` passes.
- The learner subsequently supplied terminal output from
  `project-materials/exercises/workspaces/m01-reservations/` showing
  `.\.venv\Scripts\python.exe --version` returned `Python 3.15.2`.
  This meets the disclosed step 2 environment-availability check; it does not
  establish fresh-environment reproduction or independent coding mastery.
  He explicitly chose Visual Studio Code. Read-only inspection also found the
  workspace and `.venv` directory, and the working tree was clean before this
  record update. The mentor did not execute the interpreter for him.
  The next task explains selecting the exercise interpreter and checking its
  executable path in a new integrated terminal; results were pending then.
- The learner supplied `python -c "import sys; print(sys.executable)"` output
  pointing to the exercise's `.venv/Scripts/python.exe`, with the terminal
  located at the repository root. This establishes the required terminal
  interpreter resolution; the mentor did not inspect the editor UI. The output
  prompt contains `(.venv)`, but the shell type is not established from this alone.
  Do not assume PowerShell-specific syntax works in the learner's current shell.
- The learner requested a single repository-wide collection of useful commands,
  rather than a separate reference for every task or module. The mentor created
  [COMMANDS.md](COMMANDS.md) in materials with purpose, working-directory/shell
  context, and interpretation, and recorded its maintenance rule in
  [AGENTS.md](../AGENTS.md). This reference is mentor-authored material, not
  evidence that the learner ran or mastered every listed command.
- The learner requested the next step. The mentor assigned read-only Git
  diagnostics for the exercise environment: status, the ignore-rule match for
  its Python executable, and a tracked-file listing for the entire `.venv/`
  directory. The shared reference was adjusted to cover the directory-level
  tracking check. At assignment, actual outputs and interpretation were pending;
  the mentor did not run these exercise diagnostics for him.
- The learner supplied the Git diagnostic outputs. The successful ignore check
  identified `.venv/.gitignore`, line 2, pattern `*`, for the environment's Python
  executable. The corrected `git ls-files` command returned no paths under
  `.venv/`. Initial missing-path and `ls-filess` errors were corrected by the
  learner; they were command syntax errors, not evidence of conceptual failure.
  He initially could not interpret the rule source, so the mentor explained
  the verbose output format. He correctly answered that adding `*` does not
  stop existing tracking. His follow-up questions explored historical commits,
  future changes, and staging; the mentor clarified continued tracked-file
  staging under `git add --all`, staging versus committing, and exact syntax.
  He explicitly said he understood and requested continuing. The diagnostic
  check and discussion are complete; do not claim that he independently parsed
  the original rule or demonstrated untracking/commit operations. No Git repair
  or staging is needed for the observed environment.
- The mentor assigned explanation-led pytest installation through `python -m
  pip`, checking pip location before installation and pytest's version after it.
  The shared command reference was extended. All installation and command
  execution remain learner-owned; no package was installed by the mentor and
  at assignment no pytest startup, dependency-file creation, or completed M01
  was claimed.
- The learner supplied successful pip/pytest output. Pip 26.2.2 was located
  inside the assigned exercise `.venv`; the installation log reports pytest
  9.2.0 and its dependencies installed, and `python -m pytest --version`
  returned `pytest 9.2.0`. The learner also independently chose to update pip:
  a single-hyphen `-upgrade` option failed, then the corrected `--upgrade`
  command reported successful installation of pip 26.3. Treat the corrected
  option as a syntax clarification, not an unresolved failure or a required
  extra upgrade. No exercise tests have been written or run by the learner.
  The mentor assigned displaying the installed package inventory, learner
  creation of `requirements-dev.txt`, and short exercise setup notes. At
  assignment both files were still pending; fresh-environment
  reproduction and coding/test tasks remain pending.
- The learner created `requirements-dev.txt` and explicitly asked the mentor
  to create `SETUP.md`. This authorizes that documentation assistance without
  changing learner ownership of future code/tests. The inspected requirements
  contain the same six packages and versions as his installation output:
  colorama 0.4.6, iniconfig 2.3.1, packaging 26.3, pluggy 1.7.0,
  Pygments 2.21.0, and pytest 9.2.0. No separate freeze output was supplied.
  The mentor wrote English setup notes with recorded versions, shell-specific
  navigation, explicit exercise-interpreter commands, and a fresh-reproduction
  gap. This is mentor-authored documentation, not an independent learner setup
  explanation. The mentor did not modify requirements, install packages, create
  another environment, or execute code/tests.
- The owner clarified that `SETUP.md` should read like conventional GitHub
  project setup documentation. The mentor removed learning authorship, progress,
  and verification-history narration from that file, retaining prerequisites,
  setup commands, and expected versions. Learning evidence and the outstanding
  fresh-environment reproduction check remain here. The layout/documentation
  rule and the step 6 task were updated to preserve this boundary.
- The learner requested continuation after setup documentation was corrected.
  Read-only inspection found `.venv`, `requirements-dev.txt`, and `SETUP.md` in
  the exercise workspace, with no learner implementation file in the inspected
  inventory. The mentor assigned `total_minutes_for_room(reservations, room)`
  on disclosed fictional single-day reservation data. The learner will derive
  expectations before implementing a plain Python calculation in `reservations.py`.
  No numeric answers, implementation, test code, or execution were supplied by
  the mentor. Automated tests follow review of this first implementation attempt;
  learner reasoning and assistance must remain distinguished.
- The learner requested a model of a different function, rather than a close
  copy of the reservation algorithm, and mandatory argument/return annotations.
  The mentor provided a greeting function using string/boolean arguments and
  a string result, explaining definition, branches, indentation, f-strings,
  local variables, return, and annotation limits. The current exercise's broad
  list/dictionary/union annotation was also introduced explicitly, with its
  limited field precision acknowledged; no static-checker pass is assigned yet.
  At that point the observed `reservations.py` contained only the supplied data;
  the mentor did not change it or supply the reservation function's body or
  numeric answers. Example outputs were manually reasoned, not run. This is
  requested instructional scaffolding, not evidence of learner implementation
  or demonstrated mastery. The annotation requirement is recorded in
  [AGENTS.md](../AGENTS.md) and the active task.
- The learner reported updating requirements for notebook support. The current
  file includes ipykernel/IPython and related dependencies; this inspection
  does not independently verify a new freeze/environment comparison.
  He then submitted his own annotated function using two list comprehensions,
  an explicit absent-room return, and `sum(durations)`, and requested an
  explanation of a Pylance underline plus the mentor's preferred implementation.
  That explicit request permits discussing a complete reference alternative;
  it does not authorize rewriting his source file.
- The mentor ran the inspected learner file in the exercise interpreter with
  bytecode writing disabled, capturing its top-level print. Results: A = 60,
  B = 50, C = 0, empty list = 0; outputs are integers, the supplied data stays
  unchanged, and reversing row order preserves A's total. Loading the file
  prints `60` because the example call is at module scope. These are mentor
  verification checks, not learner-written pytest evidence or complete M01.
  No benchmark or static type-checker run was performed. The exact Pylance
  diagnostic was not supplied/observed. The broad mentor-proposed dictionary
  annotation permits string durations, so type inference plausibly produces
  `list[int | str]` for `durations`. Explain this as a limitation of the supplied
  baseline, not a failure to meet an unannounced stricter typing requirement.
  Discuss TypedDict as an explicitly introduced option for precise fields,
  removal of redundant scans, and a sum/generator alternative. Do not finalize
  disputed feedback or mark the task complete before the discussion concludes.
- The learner subsequently asked about ordinary dictionaries versus TypedDict.
  Inspection showed the reference body was applied but the global data list
  lacked its annotation. The mentor explained runtime dictionaries versus static
  shape information and directed moving the type definition before the data
  and adding `list[Reservation]`. At the next continuation request, both changes
  were present. This is an assisted refactor applied by the learner; do not claim
  he independently designed the reference algorithm or precise record typing.
- The mentor rechecked the updated function with the exercise interpreter and
  bytecode writing disabled: A = 60, B = 50, C = 0, empty list = 0, all integers;
  input data stayed unchanged. Module loading still printed `60`. No actual
  Pylance diagnostic or static-checker success is claimed. No learner test file
  was found in the inspected inventory. The mentor assigned an explained import
  guard and three learner-owned pytest cases, with self-prepared normal-case
  data and manual expected-value reasoning. The generic greeting test and
  import/runner syntax are scaffolding, not reservation-test solutions.
- On 2026-11-08 the learner submitted `test_reservations.py` and terminal output
  from `.\.venv\Scripts\python.exe -m pytest -q test_reservations.py` showing
  `3 passed in 0.01s`. The mentor inspected the source and tests and reran the
  same file through the exercise interpreter with `-B` and `-p no:cacheprovider`
  to avoid writing bytecode or pytest cache; result: `3 passed in 0.01s`.
  The source's example print is now guarded by `if __name__ == "__main__"`.
  The tests assert B = 50 for durations 35 and 15 while excluding A = 20,
  C = 0 for a nonempty A/B list, and A = 0 for an empty list. All test functions
  have return annotations and independently declared inputs, rather than
  importing the source module's sample list. The data values reuse sample
  records; novel numerical values are not required for these checks to work.
  Each test is also called at module scope and its `None` return assigned to
  `test_1`, `test_2`, or `test_3`, causing execution during import as well as
  pytest execution. The learner should remove those manual calls and move each
  input list into its test as specified, preserving its type annotation.
  The learner reported additional direct calls to the calculation function;
  these are extra execution checks, not an independent expected-value derivation.
  The mentor verified the stated totals by reading the data; no explicit learner
  manual calculation has yet been supplied. Explain this distinction without
  assuming that the learner obtained his hard-coded expectation from the function.
  Earlier discussion clarified implicit `None`, assertions, and pytest's report;
  the command reference and task now explicitly explain the result display and
  runner ownership. The mentor did not edit learner source or tests. Step 8
  remains under review; no full M01 completion or fresh-environment run is claimed.
- The learner then submitted the requested corrections. All three annotated
  input lists are now inside their corresponding test functions, and the
  module-scope test calls have been removed. The mentor inspected the full
  source and test files and reran pytest with the same cache-suppressing options:
  `3 passed in 0.01s`. Requested code corrections are accepted. The first two
  list literals still have inconsistent visual indentation inside brackets;
  this is a formatting note, not a new functional acceptance requirement.
  No learner code was edited by the mentor, and no new learner-run output or
  explicit manual expected-value derivation was supplied in this submission.
- On the learner's request to continue, inspection found no exercise pytest
  configuration file. The mentor introduced an exercise-local `pytest.ini`,
  INI section/assignment syntax, `testpaths`, `addopts`, default discovery versus
  explicit paths, and a separate collection inspection with a temporary options
  override. Official pytest documentation and the installed runner's help were
  checked. The task requires the learner to create the configuration and show
  its selection, three collected tests, and a separate three-test passing run.
  The shared command reference was extended. No learner configuration, source,
  tests, environment, or dependency file was created or changed by the mentor;
  no configuration verification or new learner execution is claimed.
- The learner requested a concrete INI example, so the mentor supplied the
  complete three-line configuration in chat. The learner created `pytest.ini`;
  inspection confirms `[pytest]`, `testpaths = .`, and `addopts = -q`.
  His collection output identifies the workspace as `rootdir`, `pytest.ini`
  as `configfile`, `testpaths: .`, and exactly the existing three test functions.
  His separate invocation without a test path or `-q` reports
  `3 passed in 0.01s`. Step 9 configuration and execution requirements are met
  with disclosed reference assistance; independent configuration design or a
  separate learner explanation of the two settings is not claimed. No redundant
  mentor test run, dependency change, or environment recreation was needed.
- On continuation, the mentor inspected the workspace inventory, tracked and
  untracked paths, and a small tracked-document patch. No workspace files are
  currently indexed; Git lists source, tests, `pytest.ini`, requirements,
  `SETUP.md`, `dev_sandbox.ipynb`, and two generated `.pyc` files as untracked.
  The notebook's contents and intended role were not inspected. No workspace
  ignore file is present. `SETUP.md` still covers installation and tool checks
  but not normal function/test execution. The mentor assigned a focused inventory
  and patch review, explained status/diff notation and generated bytecode, and
  extended the shared commands. Follow-up scope includes learner-written cache
  exclusion and status verification after discussing file selection; operational
  documentation remains a later step. No staging, commit, deletion, ignore-file
  edit, or learner review is claimed. Other existing changes remain preserved.
- The learner supplied both requested Git outputs. Status confirms the eight
  untracked workspace files, including two `.pyc` files. The tracked-document
  diff adds an outcome paragraph; Git also displays a line-ending conversion
  warning, not an execution failure. The learner has not yet supplied file
  selection, the notebook's intended role, or a description of the patch.
  Inspection confirms no workspace `.gitignore` and no indexed cache files.
  The mentor assigned creating an exercise-local `.gitignore` with the explained
  `__pycache__/` rule and repeating status, preserving generated files on disk.
  No learner ignore edit, resulting status, or untracking action is claimed.
- The learner objected to advancing before his review answers were discussed;
  the mentor deferred the ignore-file instructions. He then chose to retain
  task-document changes and the listed workspace files except generated caches
  and `dev_sandbox.ipynb`, explaining that the notebook is no longer needed.
  This is a file-selection decision, not an explicit deletion request. He stated
  that he does not know how to read the diff. Teach the format using his supplied
  patch, distinguishing headers, old/new line ranges, context, and added/removed
  content, before assessing his interpretation or resuming ignore changes.
  Do not infer diff-reading understanding from command execution. No notebook
  deletion, ignore edit, staging, or completed review is claimed.
- After the explanation, the learner correctly described `Outcome` as recording
  progress and completed work, updated after advancing in learning. This meets
  the requested meaning-of-change check with the supplied notation explanation;
  no independent prior diff-reading skill is claimed. All three review answers
  have now been discussed. Inspection still finds no workspace `.gitignore`
  and lists generated caches plus the unwanted sandbox as untracked. Resume
  the learner-owned ignore follow-up: exclude `__pycache__/` and the specifically
  named `dev_sandbox.ipynb`, preserving files on disk, then inspect status.
- The learner created the workspace `.gitignore` and supplied a follow-up status
  listing exactly six untracked candidates: `.gitignore`, `SETUP.md`, `pytest.ini`,
  `requirements-dev.txt`, `reservations.py`, and `test_reservations.py`.
  Inspection confirms the explained rules `__pycache__/` and `dev_sandbox.ipynb`.
  Mentor `git check-ignore -v` checks identify those two rules for a cache file
  and the notebook; `git ls-files` returns no indexed cache/notebook paths.
  Step 10 is complete within the disclosed workspace-inventory and single-patch
  review scope, with notation and ignore syntax supplied by the mentor. This is
  not a review of every unrelated repository change. No staging, commit, file
  deletion, source edit, or new test run was performed.
- The learner explicitly requested updating `SETUP.md` and a summary of changes.
  The mentor read the setup notes, source, tests, and pytest configuration, then
  executed the documented commands in the existing exercise environment:
  `.\.venv\Scripts\python.exe reservations.py` printed `50`;
  `.\.venv\Scripts\python.exe -m pytest` reported `3 passed in 0.01s`.
  English operational notes now include a table of contents, the working
  directory, direct script execution and its expected room-B total, and the
  configuration-based test command with expected count and covered cases.
  The script command was also added to the shared command reference. Learning
  authorship and execution evidence remain here, outside the operational notes.
  This is requested mentor-authored documentation with verification in the
  existing environment, not learner-authored code or fresh-environment evidence.
  No source, tests, dependencies, configuration, or environment were changed.
- On continuation, the mentor inspected current requirements, setup notes, and
  ignore rules and confirmed `.venv-repro` does not exist. Official venv and
  freeze documentation were checked. A staged reproduction task was prepared:
  the learner first creates an additional environment, verifies its Python and
  executable path, and inspects freeze before any exercise-package installation.
  The shared commands explain the new environment prefix and expected empty
  baseline, including pip's default omission from freeze. Installation and
  execution are later stages, after discussing baseline outputs. This checks
  fresh packages with the existing source and host, not a clean checkout or
  cross-platform reproducibility. No environment, installation, learner command
  execution, or completed M01 is claimed by preparing these materials.
- The learner supplied successful `.venv-repro` creation and baseline outputs:
  Python 3.15.2, an executable path under the exercise's `.venv-repro/Scripts/`,
  and no freeze package lines. Inspection of its `pyvenv.cfg` confirms version
  3.15.2 and `include-system-site-packages = false`. Stage 1 is accepted.
  The mentor assigned the recorded pip/requirements installation, pip-path and
  inventory checks, and example/pytest execution through the new interpreter,
  with expected `50` and `3 passed`. Installation errors must be discussed
  before advancing. No mentor package installation, learner stage-2 execution,
  successful reproduction, or completed M01 is claimed yet.
- The learner supplied stage-2 terminal output as a chat attachment. It shows
  successful installation of pip 26.3, installation from `requirements-dev.txt`,
  a post-install freeze, example output `50`, and `3 passed in 0.01s`, all through
  `.venv-repro/Scripts/python.exe`. The mentor compared the pasted freeze with
  the current requirements file: all 31 pinned entries match, with no differences.
  The attachment omits a standalone pip-version diagnostic; the mentor ran that
  read-only check and confirmed pip 26.3 inside `.venv-repro/Lib/site-packages`.
  No redundant test run or installation was performed by the mentor.
  Fresh-environment reproduction is accepted on this Windows host with the
  existing exercise source; notebook execution, a clean checkout, and other
  platforms were not tested. M01's technical work is complete. File-selection
  understanding is already evidenced; ask only for the remaining concise
  explanation of why the explicit reproduction-interpreter path was used
  instead of unqualified `python`. Do not infer that explanation from command
  execution or claim it has been supplied. M01 remains active until reviewed.
- The learner explained that the explicit interpreter path ensures use of the
  intended virtual environment and its isolation from the global Python setup.
  This satisfies the remaining M01 interpreter-selection explanation. His
  `venv-report` wording is treated as a naming slip; the executed paths and
  inspected environment are `.venv-repro`. Together with fresh-environment
  execution and the earlier reasoned Git/file selection, M01 acceptance is met.
  M01 is complete on 2026-11-08; M02 has not started. Reference algorithm/typing,
  configuration examples, and mentor-authored documentation remain recorded as
  assistance rather than independently designed learner work. No extra test,
  installation, cleanup, Git mutation, or main-project work was performed.

## Next Action

On continuation, begin M02 under [LEARNING.md](../project-guidance/LEARNING.md#m02--engineering-concepts-and-readiness):
use a deliberately mixed fictional reservation script to practise separating
responsibilities/interfaces, validation, and test levels. Explain and disclose
the next task before learner implementation. No M02 workspace or starter script
has been created yet. M00 and M01 prerequisites are complete.
Reproduction and the closing explanation under
[m01-11-environment-reproduction.md](exercises/tasks/m01-11-environment-reproduction.md)
are accepted. Do not repeat completed Git/file-selection or interpreter
questions, arithmetic, installations, or tests.
Keep `.venv`, `.venv-repro`, and source files; no cleanup was requested.
Use the completed [SETUP.md](exercises/workspaces/m01-reservations/SETUP.md)
with the explained environment-prefix substitution. The workspace review under
[m01-10-git-review.md](exercises/tasks/m01-10-git-review.md) is complete, including
file selection, assisted patch interpretation, ignore rules, and resulting
status; do not reassign it or infer a review of every repository change.
The ignored notebook was preserved; no deletion, staging, or commit is authorized.
The assisted configuration step under
[m01-09-pytest-configuration.md](exercises/tasks/m01-09-pytest-configuration.md)
is complete using the inspected file and learner-supplied collection and passing
run; do not reassign it. The revised first-test code passes review; requested
local-data and runner corrections are verified and must not be reassigned.
Keep the independent-expectation evidence limit explicit without
assuming how the learner chose his existing value or repeating the same
arithmetic as a conceptual quiz. Distinguish mentor reference code from
learner-owned test reasoning.
M01 fresh-environment reproduction, operational documentation, and the final
interpreter-selection explanation are complete.
Do not repeat the completed Git discussion or invent dependency versions/results.
Do not repeat the completed terminal-interpreter check or require 3.14.
Use the shared [COMMANDS.md](COMMANDS.md) for command lookup and extend it when
introducing reusable commands. Account for PowerShell versus CMD syntax where
relevant. Treat setup errors as troubleshooting evidence.
Do not create the environment or implement the learner's function/test for him.
The M00 final review and feedback are recorded; do not repeat completed questions.
Support Python syntax/functions and modularity during practical tasks as needed.
Do not add a separate preliminary Python refresher course.
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
M00 and M01 acceptance are complete; main-project work remains blocked until
M02 readiness is demonstrated.
