# M00 Part 4 Understanding Feedback

Reviewed: 2026-10-29 (Europe/Warsaw). Source: the learner's chat answers to
[m00-04-environment-configuration-and-notebook-state.md](../lectures/m00-04-environment-configuration-and-notebook-state.md).

## Interpreter Selection

The learner correctly identified different terminal/notebook interpreters as
the likely cause of a library importing in the terminal but not the notebook.
He correctly explained why reinstalling into the same terminal environment
would not solve a missing package in another environment.

Refinement delivered: either select the intended, already prepared environment
for the notebook or install the required package into the environment the
notebook intentionally uses. First verify the interpreter selection; an import
failure alone does not prove this particular cause. No installation is performed.

## Notebook State

The learner correctly explained that skipping cell 2 leaves `total` unchanged
after changing `durations`. He correctly proposed restarting and running all
cells from the beginning to check independence from retained session state.

Terminology refinement: the kernel holds `total` in memory; cell 2 contains
the code that calculates and assigns it. The learner's references to `Total`
and `Durations` in prose are treated as references to the disclosed code, not
as a submitted case-sensitive implementation error.

Both part 4 conceptual checks are met. No command execution, actual environment
setup, or independent M01/M02 readiness is inferred. Continue M00 with pandas
table inspection, filtering, and grouping; joins and charts follow separately.
