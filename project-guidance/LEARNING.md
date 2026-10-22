# Engineering Core Learning Guide

Use the learning record to choose the active phase/unit; read that section and
its prerequisites. [PROJECT.md](PROJECT.md) owns the analytical scenario, data,
product requirements, and acceptance. This file owns teaching and learning evidence.

## Table Of Contents

- [Delivery And Readiness](#delivery-and-readiness)
- [Learning Record And Resumption](#learning-record-and-resumption)
- [M00 — Goal And Starting Point](#m00--goal-and-starting-point)
- [M01 — Environment And Repository](#m01--environment-and-repository)
- [M02 — Engineering Concepts And Readiness](#m02--engineering-concepts-and-readiness)
- [M03 — Source Audit And Sample](#m03--source-audit-and-sample)
- [M04 — Independent EDA](#m04--independent-eda)
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

Follow this delivery order:

| Phase | Units, in delivery order |
| --- | --- |
| Theoretical introduction | M00 |
| Independent exercises | M01 → M02 |
| Main project | M03 → M04 → M05 → M06 → M07 → M08 → M09 → M10 → M11 → M12 |

A brief scope/starting-skill diagnosis precedes teaching; it cannot
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
attempts, and feedback in `project-materials/exercises/`;
[AGENTS.md](../AGENTS.md) owns the full artifact layout and language rules.
Adapt task size and explanations to observed gaps without replacing learner-owned
work. Prior experience may shorten, not
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
For records from older packs, map units by topic: former M04 engineering exercises
→ M02, M02 source audit → M03, and M03 EDA → M04; all other IDs are unchanged.
Update record references without discarding evidence or repeating completed work.
Prepared documents, generated artifacts, and agent execution alone prove neither
delivery nor learning.

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

**Requires:** completed [M00 introduction](#m00--goal-and-starting-point).
Guide setup in the independent exercise area: interpreter/virtual environment,
dependencies, imports/paths, minimal configuration, Git ignore/tracked files,
a function with a pytest test, setup notes, and diff review.

**Pass:** the learner reproduces setup and function/test execution in a fresh
environment and explains interpreter selection and version-controlled files.

## M02 — Engineering Concepts And Readiness

**Requires:** completed [M01](#m01--environment-and-repository) and
[M00](#m00--goal-and-starting-point), no project data.
Use a deliberately mixed reservation script to practise responsibility/interface
separation, validation, and test levels. The learner designs three edge-case
validations/tests: duplicate reservation ID, wrong duration unit, negative duration.

**Pass:** exercise code, responsibility/interface plan, and three validations/tests
exist; the learner explains design/testing and demonstrates independent reasoning
or a tested change. Record readiness before M03; no bicycle components are created.

## M03 — Source Audit And Sample

**Requires:** verified [M02 readiness](#m02--engineering-concepts-and-readiness)
and real source access.
Guide the learner's audit against [PROJECT.md](PROJECT.md#source-verification):
statistical dimensions/CN8, indicators, units, flags, filtering, and revisions.
A verified export/API retrieval is enough here; automation belongs to M06.

**Pass:** audit notes and the agreed 2017–2025 snapshot/manifest exist; the learner
explains grain, code mapping, units, and limitations. Unresolved comparability
blocks affected calculations; access failure remains a blocker, not a synthetic audit.

## M04 — Independent EDA

**Requires:** the [M03 snapshot](#m03--source-audit-and-sample).
The learner writes the notebook exploring grain/types, ranges, duplicates,
missingness/flags, expected coverage, selected series, and a manually traced
aggregation. Explain pandas/charts as needed and review without writing the EDA.

**Pass:** a fresh-kernel run works; the learner explains quality findings,
justified calculations, and consequences for the contract.

## M05 — Contract And Validation

**Requires:** completed [M03](#m03--source-audit-and-sample) and
[M04](#m04--independent-eda), with verified
[M02 readiness](#m02--engineering-concepts-and-readiness).
The learner translates audit/EDA findings into normalization, a documented contract,
validation, and a quality report under [PROJECT.md](PROJECT.md#data-contract).
Add tests with components; cover valid input, duplicate keys, wrong units,
invalid ranges, missing months/values, and genuine zeros.

**Pass:** contract, code, report, and tests agree; the learner independently adds
a validation and explains its failure behavior and why annotations cannot replace it.

## M06 — Repeatable Acquisition

**Requires:** completed [M05](#m05--contract-and-validation) and verified
[M03 retrieval](#m03--source-audit-and-sample).
Guide acquisition/manifest automation: input/output boundaries, request configuration,
timeouts/network and malformed-response handling, checksums, and immutable snapshots.
Test with network fakes; keep requests bounded and TLS enabled.

**Pass:** acquisition command/tests work without overwriting earlier snapshots;
the learner explains why local recalculation is independent of source revisions.

## M07 — Business Logic

**Requires:** completed [M05](#m05--contract-and-validation) and
[M06](#m06--repeatable-acquisition).
Apply pure functions, aggregation/joins, denominators, and comparable periods to
[PROJECT.md](PROJECT.md#measures-and-interpretation). For each measure, require
a small manual calculation and independent expected result before implementation.

**Pass:** functions/tests/tables cover the agreed formulas and edge cases;
the learner explains denominators and changes a calculation on a new sample.

## M08 — Orchestration And Reliability

**Requires:** completed [M07](#m07--business-logic).
Guide configuration, command interfaces, typed production boundaries, exception
handling, and logging in the local pipeline.

**Pass:** one command processes the snapshot with the failure behavior required
by [PROJECT.md](PROJECT.md#deliverables-and-technical-requirements); the learner
traces the flow, diagnoses an error, and explains static typing's limits.
Charts/report generation extend this command in M11.

## M09 — Integration And Reproducibility

**Requires:** completed [M08](#m08--orchestration-and-reliability) and existing
component tests.
Consolidate offline integration coverage from source response to outputs,
using fixtures, temporary directories, and fakes. Check corrupt input,
incomplete years, failures without success artifacts, and repeated-run equality.

**Pass:** integration/repeatability evidence meets
[PROJECT.md](PROJECT.md#product-acceptance) requirements; the learner
chooses and explains a test level for a new failure case. Extend coverage to the
report in M11.

## M10 — Quality Gate And CI

**Requires:** completed [M09](#m09--integration-and-reproducibility).
Guide Ruff lint/format, production-code type checks, pytest, and matching offline
GitHub Actions. Use a controlled error to identify each check's responsibility;
fix causes rather than hide failures with broad exclusions.

**Pass:** local checks and actual CI pass for the reviewed version, with the learner
explaining their limits. If remote execution is blocked, retain the CI acceptance
gap and continue local reporting; a workflow file alone is not a passed run.

## M11 — Business Report

**Requires:** passing [M10 local checks](#m10--quality-gate-and-ci) and verified
results. An unresolved CI gap permits local reporting, not final acceptance.
The learner owns interpretation, chart/table selection, units, uncertainty, and
traceability. Support editing of a concise report answering the research question,
with limitations and follow-up questions; include generation in integration tests.

**Pass:** one command produces the dataset, quality report, agreed measures,
tables/charts, and business report. The learner defends two findings and identifies
extra evidence required for a purchasing decision.

## M12 — Handover And Independent Change

**Requires:** completed [M11](#m11--business-report).
The learner completes README under [MAINTENANCE.md](MAINTENANCE.md#project-readme),
checks it from a clean copy/fresh environment, and makes a small independent
tested change. Use hints/review rather than performing that change.

**Pass:** product and learning acceptance have evidence; the learner explains
design decisions, their change, lessons learned, and areas needing practice.
Git actions and publication remain subject to
[AGENTS.md](../AGENTS.md#safety-and-approval).

## Final Acceptance

Verify [PROJECT.md](PROJECT.md#product-acceptance) and README presentation rules in
[MAINTENANCE.md](MAINTENANCE.md#project-readme), recording actual commands/results
and the accepted version's CI run reference. Re-run the M10 quality gate for the
final version, including M11 report generation and the M12 independent change;
an earlier passing run does not verify later changes. Keep acceptance incomplete
while required evidence, including actual CI, is missing.
In addition, require evidence that:

- M00 theory was delivered and M01 → M02 exercises demonstrated readiness before
  main-project work; preparation artifacts remain separate from project outputs.
- EDA, analytical decisions, and report interpretation are learner-owned; assisted
  work is identified. The learner explains responsibilities, contracts, typing
  versus runtime validation, and test levels.
- The learner demonstrates an independent tested change and explains it.

Record acceptance evidence, remaining gaps, and next action in the single
learning record; generated or agent-written artifacts alone do not establish completion.
