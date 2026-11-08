# M01 Step 5 — Install And Inspect Pytest

Prerequisites: the exercise interpreter is available and verified; Git ignore
and tracking diagnostics were reviewed under
[m01-04-git-ignore.md](m01-04-git-ignore.md).

Outcome: learner-supplied output confirms pip was in the exercise environment,
pytest 9.2.0 was installed, and `python -m pytest --version` returned that version.
He also updated pip from 26.2.2 to 26.3 after correcting `-upgrade` to `--upgrade`.
No exercise test run is established by version inspection. Continue with
[m01-06-dependencies-and-setup-notes.md](m01-06-dependencies-and-setup-notes.md).

## Purpose

A package is installable reusable code. `pip` installs Python packages;
`pytest` discovers and runs automated tests. Installing pytest is preparation
for the learner's function/test task, not evidence that any test has passed.

The interpreter is Python 3.15.2 in
`project-materials/exercises/workspaces/m01-reservations/.venv/`. Use the terminal
already verified to resolve `python` to that environment. The working directory
may remain the repository root; these commands select their environment through
the interpreter, not the current directory. PowerShell and CMD are both suitable.

## Task

First inspect pip through the selected interpreter:

```console
python -m pip --version
```

`-m` executes a module using this Python interpreter. The output includes pip's
version and package location. Confirm that the location is under the exercise's
`.venv` before proceeding. If pip is missing or the location is outside that
environment, report the output before installing or modifying anything else.

Then install pytest:

```console
python -m pip install pytest
```

This command downloads and installs pytest and its dependencies into the
selected environment. Dependencies are other packages pytest needs. No global
installation, new tool manager, or pip upgrade is assigned.

Finally check pytest through the same interpreter:

```console
python -m pytest --version
```

This starts the installed pytest tool and reports its version without running
exercise tests. Send the first and final command outputs, confirm installation
succeeded, or report an error at the step where it occurs. Do not infer a passed
test from a successful version display.

Reusable command explanations are in
[COMMANDS.md](../../COMMANDS.md#packages-and-test-tools).

## Completion Criterion And Next Step

The learner identifies pip inside the exercise environment and supplies the
actual installed pytest version. The mentor has not performed these operations.
Then guide recording dependencies and setup instructions before assigning the
learner's function and test. A documented fresh-environment check remains later
M01 work; observing versions alone does not establish reproducibility.

Sources: [Running pip](https://pip.pypa.io/en/stable/user_guide/#running-pip),
[Installing pytest](https://docs.pytest.org/en/stable/getting-started.html#install-pytest).
