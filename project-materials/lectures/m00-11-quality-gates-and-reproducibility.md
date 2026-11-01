# M00 Part 11 — Quality Gates And Reproducibility

This completes the planned lecture coverage after
[m00-10-testing-and-independent-expectations.md](m00-10-testing-and-independent-expectations.md).
It remains M00 theory. Tool behavior was checked against official documentation;
no quality gate or reproduction procedure is run, no environment/workflow is
configured, and no source acquisition or analysis is performed. Operational
names below are illustrations, not validated
commands for the current repository. M00 completion still requires discussion
of the understanding check. M01 additionally requires the owner's explicit
confirmation, recorded in [PROGRESS.md](../PROGRESS.md).

## Contents

- [Different Checks Answer Different Questions](#different-checks-answer-different-questions)
- [A Quality Gate Has A Defined Scope](#a-quality-gate-has-a-defined-scope)
- [Continuous Integration And Evidence](#continuous-integration-and-evidence)
- [Fresh-Environment Reproduction](#fresh-environment-reproduction)
- [README As A Verified Handover](#readme-as-a-verified-handover)
- [Connecting The Introduction To The Project](#connecting-the-introduction-to-the-project)
- [Final M00 Understanding Review](#final-m00-understanding-review)
- [References](#references)

## Different Checks Answer Different Questions

A linter examines code against configured rules for suspicious constructs,
common mistakes, and conventions. Ruff's linter is invoked through `ruff check`;
depending on the enabled rules it can identify unused imports or undefined
names. This is static code inspection, not execution of reservation calculations.

A formatter arranges code into consistent layout, such as spacing, quotes, and
line breaks. Ruff provides `ruff format`, while `ruff format --check` checks
formatting without rewriting files. Consistent formatting reduces distracting
differences during review. A beautifully formatted wrong calculation remains wrong.

A type checker such as mypy or Pyright checks type consistency, as discussed
in part 8. The production-code paths and configuration must be explicit. pytest
runs the behavioral tests explained in part 10. Runtime validation still checks
actual input against the data contract when the process runs.

| Check | Primary evidence | Important limit |
| --- | --- | --- |
| Ruff lint | Examined code satisfies enabled rules | Does not establish correct business results |
| Ruff format check | Examined code matches the formatting convention | Does not validate calculations |
| Type checker | Examined typed code has no reported type inconsistency | Simple types do not establish units or source quality |
| pytest | Collected tests satisfy their expectations | Only the tested cases and behaviors are covered |
| Runtime data validation | Delivered data satisfies implemented checks | Checks need correct requirements and implementation |

## A Quality Gate Has A Defined Scope

A quality gate is the agreed set of checks that must pass for a particular
acceptance decision. It needs defined tool versions, rules, code/test paths,
configuration, and failure criteria. A tool reporting success for excluded
code does not establish that code's correctness. Read which files and tests
were actually examined.

If a check fails, investigate the cause before deciding whether code, tests,
or configuration should change. A narrow justified exclusion can be legitimate;
excluding a whole failing area solely to obtain green status reduces the
evidence. Changing business expectations to fit a bug has the same problem.
Tool results do not replace review of the contract, input snapshot, outputs,
and interpretation.

In the reservation example, lint, formatting, and type checks may all pass for
code that double-counts a joined reservation. A well-designed test can detect
that particular fault. Conversely, even tests may pass if their expectations
repeat the same faulty assumption. State what the evidence supports.

## Continuous Integration And Evidence

Continuous integration (CI) is the practice of regularly integrating changes
and automatically checking the shared code. GitHub Actions can run a configured
workflow, meaning a defined automation process, in response to a push, a pull
request, or another configured event. A runner is the machine executing its
jobs. A pull request proposes merging changes into another branch.

For our learning examples, a workflow might obtain the code, recreate a specified
Python environment, install declared dependencies, and run the same lint,
format, type, and offline test checks used locally. The workflow should preserve
failure status rather than turn a failing stage into overall success. Network
access needed to obtain dependencies is separate from keeping analytical tests
independent of live data sources.

Local/remote consistency matters: different versions, checked paths, or settings
can explain different outcomes. Automation should expose these differences,
not hide them. A workflow file is a recipe; evidence of execution is a real run
with recorded results tied to the evaluated code version. A passing run for
commit A does not verify later changes in commit B. A commit identifies a saved
version of repository changes. Record the relevant version and run reference.

This lesson does not create a workflow, commit, push, or trigger remote execution.
Those actions retain their own authorization boundaries. Passing CI alone also
does not demonstrate correct real-source definitions or acceptable report claims.

## Fresh-Environment Reproduction

A successful run on the author's computer may rely on an undeclared package,
an untracked local file, a remembered environment variable, or notebook state.
A clean-copy check obtains the specified repository version in a separate
location and follows the documented setup. A fresh-environment check recreates
the interpreter/package environment from its declared specification rather
than relying on the author's installed packages.

Then obtain the exact identified input snapshot, verify its checksum, apply
the recorded configuration, and run the documented process. Compare numerical
outputs and required failure behavior. A source address yielding today's revised
data does not necessarily reproduce yesterday's report. A fresh notebook kernel
checks a different layer: retained session state, not undeclared package
availability. Clearing a kernel does not remove external files or recreate the
software environment.

Preserve exact source input or provide a verified way to obtain that exact
version, respecting source rights and access constraints. Identical numerical
results need not imply byte-identical report files if run timestamps differ.
State what reproducibility means for the acceptance decision and actually
perform the corresponding checks during the later implementation stages.

## README As A Verified Handover

A README is the entry point another person uses to understand the problem and
operate the delivered project. It should explain purpose/scope, required
environment, exact snapshot access, setup and run/check commands, outputs,
limitations, and common failures. Write commands and version claims after
they are implemented and verified, rather than presenting plans as successful
execution. Project presentation rules are owned by
[MAINTENANCE.md](../../project-guidance/MAINTENANCE.md).

Test the instructions from a clean copy or fresh environment. If a required
input exists only in the author's ignored local directory, the handover is
incomplete even when all unit tests pass. If a dependency is missing from
the setup instructions, document and fix the dependency definition rather
than merely relying on a manual local installation. Tracked files and a
clear recipe make the process transferable.

The report has another audience: it answers the analytical question using
traceable results, units, scope, completeness, and limitations. README operating
instructions and report findings complement each other. Neither an impressive
report nor a green check alone establishes full delivery acceptance.

## Connecting The Introduction To The Project

The approved question in [PROJECT.md](../../project-guidance/PROJECT.md) is how
trade in conventional and electric cycles changes in Poland compared separately
with Germany and the Netherlands. The scope is monthly Eurostat COMEXT data
for 2017–2025, imports and exports separately, WORLD partner scope, nominal EUR
and quantities in pieces, using two selected product categories. Historical
definitions, actual availability, units, flags, and reuse rights still require
the later source audit. The selected categories do not represent the entire
bicycle market, and the electric category also includes specified tricycles
and quadricycles.

The planned product includes an auditable snapshot and contract, exploratory
analysis, validated monthly data and quality reporting, agreed calculations,
charts/tables, a concise business report, reproducible execution, tests and
quality checks, and verified operating documentation. Forecasting, machine
learning, dashboards, web applications, and purchasing recommendations are
outside this delivery. Trade values do not by themselves measure retail demand
or determine ordering quantities.

The teaching sequence remains M00 theory, M01/M02 independent preparation, then
main-project work after readiness is demonstrated. Completing theory is not
evidence that practical setup and implementation have already been mastered.
The owner explicitly requires confirmation before starting M01, even after
M00's final conceptual review is complete. Do not install, set up exercises,
or choose a new active unit on that basis alone.

## Final M00 Understanding Review

These are conceptual discussion prompts. No implementation, source access,
memorization of product codes, or operational execution is required. Evaluate
reasoning against the stated facts and consider justified broader context.
Discuss uncertainty before saving feedback.

1. In a fictional reservation project, acceptance requires local checks and
   an actual CI run for the evaluated code version. Local Ruff lint/format,
   type checks, and pytest pass for commit B. The workflow file exists in B,
   but the only completed CI run is for earlier commit A. What can we honestly
   claim about B, what acceptance evidence is missing, and what do green tool
   results still not establish about the analytical conclusions?
2. A colleague follows the README from a clean repository copy in a fresh
   environment. The process fails because a required package was not declared
   and the exact input snapshot existed only in the author's ignored local
   directory. The source address now provides revised data. The author's
   machine still runs successfully. What needs to be repaired and verified to
   make the documented report reproducible for the colleague?
3. Using the project scope recalled above, explain in your own words the
   question our bicycle analysis answers, the important boundaries on its
   conclusions, and what a finished, trustworthy delivery would provide.
   Which topics now need the most practical refresh for you—Python, pandas,
   Git, environment setup, tests, or something else? This reflection helps
   choose support; uncertainty about unpractised skills is not a failure.

After discussing these responses, record actual M00 completion or any specific
remaining gap. Stay within M00 afterward until the owner explicitly confirms
the transition to M01. No confirmation is requested before completing this review.

## References

Consulted on 2026-11-01. These are conceptual references, not selected project
versions or evidence that local or remote checks have run.

- [Ruff linter](https://docs.astral.sh/ruff/linter/)
- [Ruff formatter](https://docs.astral.sh/ruff/formatter/)
- [Running mypy](https://mypy.readthedocs.io/en/stable/running_mypy.html)
- [GitHub continuous integration](https://docs.github.com/en/actions/get-started/continuous-integration)
