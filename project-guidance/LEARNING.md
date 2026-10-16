# Engineering Core Learning Guide

Use the learning record to choose the active phase/unit; read that section and
its prerequisites. [PROJECT.md](PROJECT.md) owns the analytical scenario, data,
product requirements, and acceptance. This file owns teaching and learning evidence.

## Table Of Contents

- [Delivery And Readiness](#delivery-and-readiness)
- [Learning Record And Resumption](#learning-record-and-resumption)
- [M00 — Goal And Starting Point](#m00--goal-and-starting-point)
- [M01 — Environment And Repository](#m01--environment-and-repository)
- [M04 — Engineering Concepts And Readiness](#m04--engineering-concepts-and-readiness)
- [M02 — Source Audit And Sample](#m02--source-audit-and-sample)
- [M03 — Independent EDA](#m03--independent-eda)
- [M05 — Contract And Validation](#m05--contract-and-validation)
- [M06 — Repeatable Acquisition](#m06--repeatable-acquisition)
- [M07 — Business Logic](#m07--business-logic)
- [M08 — Orchestration And Reliability](#m08--orchestration-and-reliability)
- [M09 — Integration And Reproducibility](#m09--integration-and-reproducibility)
- [M10 — Quality Gate And CI](#m10--quality-gate-and-ci)
- [M11 — Business Report](#m11--business-report)
- [M12 — Handover And Independent Change](#m12--handover-and-independent-change)
- [Final Acceptance](#final-acceptance)

## Delivery And Readiness

Required order: M00 theory → M01/M04 independent exercises → M02–M03/M05–M12
main project. A brief scope/starting-skill diagnosis precedes teaching; it cannot
replace the lecture. Project work, including source audit/EDA, starts only after
verified exercise readiness. Exercise environment setup belongs to M01.

Engineering Core develops separation of responsibilities, data contracts and
validation, typing/error handling/logging, tests, reproducibility, and automated
quality checks. Starting profile: Python needs refreshing, SQL is stronger
through work, and basic Git is familiar. Verify rather than assume this profile;
use SQL analogies where useful. Rough emphasis is 20% theory/exercises,
65% implementation, 15% verification/documentation, not a time quota.

Deliver an engaging, substantive lecture as connected prose covering M00.
Explain unfamiliar terms, why/how concepts work, relationships, practical use,
limitations, and trade-offs with small examples. Humor may support clarity.
Lists, code, or diagrams may help, but a topic checklist, links, or external
reading cannot replace explanations. Split long lectures coherently, check
understanding, and finish the introduction before assigning its exercises.

Independent exercises apply already explained concepts in a different domain,
task, and data. A small synthetic dataset of meeting-room reservations, clearly
labelled as fictional, is a suitable example.
No bicycle data, Eurostat excerpt, or project component qualifies. Disclose inputs,
grain, assumptions, task, and pass criterion. Let the learner attempt, then offer
gradual hints, review, and explanation; full solutions require a request or
discussion of attempts. Require reasoning or an independent tested change,
not merely execution of agent output.

Save lectures in `project-materials/lectures/` and exercise prompts, code/data/tests,
attempts, and feedback in `project-materials/exercises/`; AGENTS owns the full
artifact layout and language rules. Adapt task size and explanations to observed
gaps without replacing learner-owned work. Prior experience may shorten, not
remove, preparation. Later explanations/exercises supplement it. The same three
phases apply to later stages extending this repository; record proposed scope
extensions without implementing them before owner approval.

## Learning Record And Resumption

Create `project-materials/PROGRESS.md` when learning begins; do not ship it as
instruction or pre-created evidence. Record current phase/unit/status, relevant
context paths, delivered lecture coverage, exercise/readiness evidence, learner
demonstrations, independent work versus assistance, language overrides,
decisions/blockers, actual checks/results, and the exact next action.

Resume from verified evidence and the active section, without replaying completed
phases. If the record is absent, reconstruct the verified state with the learner
before choosing an activity; without evidence of completed preparation, begin
with M00 and close gaps before project work. Replace current state while preserving
useful evidence; never silently reset progress or create a parallel record.
Map former unit paths to the same M00–M12 IDs in this file. Prepared documents,
generated artifacts, and agent execution alone prove neither delivery nor learning.

## M00 — Goal And Starting Point

Use the project scenario only to establish audience, question, scope, outputs,
and evidence limits; diagnose Python/SQL/Git refresh needs with a small disclosed
task. Deliver the theory using an unrelated example, without implementing the
project. Required coverage:

- Environment, dependencies, Git/configuration; notebook hidden state versus
  modules; pandas inspection, filtering, grouping, joins, and basic charts.
- Responsibilities, modularity/interfaces, input/output, validation, calculations,
  orchestration, and reporting.
- Provenance, immutable snapshots, grain/keys/units, schema/quality contracts,
  missing versus zero, and comparable aggregation.
- Type annotations versus runtime validation, exceptions, errors versus warnings,
  network boundaries/timeouts, and useful logging.
- Unit/integration tests, edge cases, independent expectations, fixtures, temporary
  directories/network fakes, regression protection, and clean-environment reproduction.
- Roles of pytest, Ruff, a type checker, continuous integration (CI)/GitHub Actions,
  README, and reports separating findings from hypotheses.

**Pass:** lecture delivery/coverage and understanding are recorded; the learner
explains the project question, boundaries, definition of done, and refresh needs.
Diagnosis alone does not complete M00.

## M01 — Environment And Repository

**Requires:** completed M00 introduction.
Guide setup in the independent exercise area: interpreter/virtual environment,
dependencies, imports/paths, minimal configuration, Git ignore/tracked files,
a function with a pytest test, setup notes, and diff review.

**Pass:** the learner reproduces setup and function/test execution in a fresh
environment and explains interpreter selection and version-controlled files.

## M04 — Engineering Concepts And Readiness

**Requires:** M01 and M00, no project data.
Use a deliberately mixed reservation script to practise responsibility/interface
separation, validation, and test levels. The learner designs three edge-case
validations/tests: duplicate reservation ID, wrong duration unit, negative duration.

**Pass:** exercise code, responsibility/interface plan, and three validations/tests
exist; the learner explains design/testing and demonstrates independent reasoning
or a tested change. Record readiness before M02; no bicycle components are created.

## M02 — Source Audit And Sample

**Requires:** M04 readiness and real source access.
Guide the learner's audit against [PROJECT.md](PROJECT.md#source-verification):
statistical dimensions/CN8, indicators, units, flags, filtering, and revisions.
A verified export/API retrieval is enough here; automation belongs to M06.

**Pass:** audit notes and the agreed 2017–2025 snapshot/manifest exist; the learner
explains grain, code mapping, units, and limitations. Unresolved comparability
blocks affected calculations; access failure remains a blocker, not a synthetic audit.

## M03 — Independent EDA

**Requires:** M02 snapshot.
The learner writes the notebook exploring grain/types, ranges, duplicates,
missingness/flags, expected coverage, selected series, and a manually traced
aggregation. Explain pandas/charts as needed and review without writing the EDA.

**Pass:** a fresh-kernel run works; the learner explains quality findings,
justified calculations, and consequences for the contract.

## M05 — Contract And Validation

**Requires:** M02–M03 and M04 readiness.
The learner translates audit/EDA findings into normalization, a documented contract,
validation, and a quality report under [PROJECT.md](PROJECT.md#data-contract).
Add tests with components; cover valid input, duplicate keys, wrong units,
invalid ranges, missing months/values, and genuine zeros.

**Pass:** contract, code, report, and tests agree; the learner independently adds
a validation and explains its failure behavior and why annotations cannot replace it.

## M06 — Repeatable Acquisition

**Requires:** M05 and verified M02 retrieval.
Guide acquisition/manifest automation: input/output boundaries, request configuration,
timeouts/network and malformed-response handling, checksums, and immutable snapshots.
Test with network fakes; keep requests bounded and TLS enabled.

**Pass:** acquisition command/tests work without overwriting earlier snapshots;
the learner explains why local recalculation is independent of source revisions.

## M07 — Business Logic

**Requires:** M05–M06.
Apply pure functions, aggregation/joins, denominators, and comparable periods to
[PROJECT.md](PROJECT.md#measures-and-interpretation). For each measure, require
a small manual calculation and independent expected result before implementation.

**Pass:** functions/tests/tables cover the agreed formulas and edge cases;
the learner explains denominators and changes a calculation on a new sample.

## M08 — Orchestration And Reliability

**Requires:** M07.
Guide configuration, command interfaces, typed production boundaries, exception
handling, and logging in the local pipeline.

**Pass:** one command processes the snapshot with the failure behavior required
by PROJECT; the learner traces the flow, diagnoses an error, and explains static
typing's limits. Charts/report generation extend this command in M11.

## M09 — Integration And Reproducibility

**Requires:** M08 and existing component tests.
Consolidate offline integration coverage from source response to outputs,
using fixtures, temporary directories, and fakes. Check corrupt input,
incomplete years, failures without success artifacts, and repeated-run equality.

**Pass:** integration/repeatability evidence meets PROJECT requirements; the learner
chooses and explains a test level for a new failure case. Extend coverage to the
report in M11.

## M10 — Quality Gate And CI

**Requires:** M09.
Guide Ruff lint/format, production-code type checks, pytest, and matching offline
GitHub Actions. Use a controlled error to identify each check's responsibility;
fix causes rather than hide failures with broad exclusions.

**Pass:** local checks and actual CI pass for the reviewed version, with the learner
explaining their limits. If remote execution is blocked, retain the CI acceptance
gap and continue local reporting; a workflow file alone is not a passed run.

## M11 — Business Report

**Requires:** M10 local checks and verified results.
The learner owns interpretation, chart/table selection, units, uncertainty, and
traceability. Support editing of a concise report answering the research question,
with limitations and follow-up questions; include generation in integration tests.

**Pass:** one command produces the dataset, quality report, agreed measures,
tables/charts, and business report. The learner defends two findings and identifies
extra evidence required for a purchasing decision.

## M12 — Handover And Independent Change

**Requires:** M11.
The learner completes README under [MAINTENANCE.md](MAINTENANCE.md#project-readme),
checks it from a clean copy/fresh environment, and makes a small independent
tested change. Use hints/review rather than performing that change.

**Pass:** product and learning acceptance have evidence; the learner explains
design decisions, their change, lessons learned, and areas needing practice.
Git actions and publication remain subject to AGENTS' separate authority.

## Final Acceptance

Verify [PROJECT.md](PROJECT.md#product-acceptance) and README presentation rules in
[MAINTENANCE.md](MAINTENANCE.md#project-readme), recording actual commands/results
and the accepted version's CI run reference. In addition, require evidence that:

- M00 theory was delivered and M01/M04 exercises demonstrated readiness before
  main-project work; preparation artifacts remain separate from project outputs.
- EDA, analytical decisions, and report interpretation are learner-owned; assisted
  work is identified. The learner explains responsibilities, contracts, typing
  versus runtime validation, and test levels.
- The learner demonstrates an independent tested change and explains it.

Record acceptance evidence, remaining gaps, and next action in the single
learning record; generated or agent-written artifacts alone do not establish completion.
