# M01 Step 9 — Configure The Test Runner

Prerequisite: the reviewed three tests from
[m01-08-first-tests.md](m01-08-first-tests.md). Continue in
`project-materials/exercises/workspaces/m01-reservations/`.
The learner creates the configuration; the mentor supplies syntax guidance
and reviews the file and actual command output.

## Table Of Contents

- [Purpose](#purpose)
- [Configuration Syntax](#configuration-syntax)
- [Task And Verification](#task-and-verification)
- [Completion Criterion](#completion-criterion)

## Purpose

The previous command explicitly selected a test file and compact output:

```console
.\.venv\Scripts\python.exe -m pytest -q test_reservations.py
```

Store exercise defaults in `pytest.ini` so a normal run only needs:

```console
.\.venv\Scripts\python.exe -m pytest
```

Pytest already discovers suitably named tests without a configuration file.
Here, the configuration makes the intended search location explicit and stores
the compact-output preference. It does not change the calculation or assertions.

## Configuration Syntax

An INI file is a text file organized into named sections and `name = value`
settings. For `pytest.ini`, use the section header `[pytest]`. The brackets
denote a configuration section; this file is not Python code.

Use these two settings below the header, each on its own line:

| Setting | Meaning |
| --- | --- |
| `testpaths` | Directories to search when running from the configuration root without explicit test paths. For this exercise, search from the directory containing `pytest.ini`; `.` denotes that directory. Discovery can descend into subdirectories under the normal pytest discovery rules. |
| `addopts` | Command-line options to apply by default. Use the already introduced compact-output option, `-q`. |

For this exercise, run commands from the workspace, which will be the
configuration root. An explicit test-file argument still selects that file;
`testpaths` supplies defaults rather than restricting every possible invocation.

## Task And Verification

1. Create `pytest.ini` beside `test_reservations.py`, outside `.venv`.
   Write the section header and the two settings described above. Do not add
   quotes around these INI values or copy Python list syntax.
2. Inspect discovery with the following command from the exercise directory:

   ```console
   .\.venv\Scripts\python.exe -m pytest --collect-only -o addopts=
   ```

   `--collect-only` finds tests without executing their bodies. Collection
   imports test modules, so module-scope statements still execute.
   `-o` temporarily overrides a configuration setting for this invocation.
   `addopts=` sets the extra default options to an empty value, allowing the
   normal startup header to be shown. It does not edit `pytest.ini`.
   Check that the header identifies `pytest.ini` as the configuration file
   and that exactly the three reservation tests are collected. Collection
   success is not a passed test run.
3. Run the shorter normal command shown under Purpose. Expect three passed
   tests and compact output, without typing `-q` or the test filename.

Send the configuration-file path and both command outputs. Briefly explain
which setting selects the default search location and which changes the report.
No new tests, dependencies, source refactor, or root-level configuration are
required. Keep the existing environment and test cases.

The shared command reference is
[COMMANDS.md](../../COMMANDS.md#run-tests-with-exercise-configuration).

## Completion Criterion

The learner writes the configuration, explains its two settings, and supplies
output identifying the configuration file, collecting the intended three tests,
and passing all three in a separate normal run. The mentor reviews the file
and output without writing the learner's configuration. A prepared task or
configuration file alone is not execution evidence. Repository diff review,
operational documentation, and fresh-environment reproduction remain later work.

Sources: [pytest configuration](https://docs.pytest.org/en/stable/reference/customize.html#pytest-ini),
[testpaths](https://docs.pytest.org/en/stable/reference/reference.html#confval-testpaths),
[addopts](https://docs.pytest.org/en/stable/reference/reference.html#confval-addopts),
[command-line options](https://docs.pytest.org/en/stable/reference/reference.html#command-line-flags).
