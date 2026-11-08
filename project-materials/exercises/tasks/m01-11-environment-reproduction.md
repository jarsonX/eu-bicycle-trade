# M01 Step 11 — Reproduce The Environment

Prerequisites: the reviewed exercise code/tests, accepted pytest configuration,
and Git review under [m01-10-git-review.md](m01-10-git-review.md).
Operational setup and usage are documented in
[SETUP.md](../workspaces/m01-reservations/SETUP.md).

## Purpose And Boundaries

Verify that the recorded dependencies support running the example and tests
in a newly created environment. Use `.venv-repro` beside `.venv`, keeping the
existing environment and exercise files. In the setup procedure, substitute
`.venv-repro` for the environment directory and executable-path prefix.
The mentor explains this adaptation; the learner performs the commands.

This checks fresh-environment reproduction with the same source files, Python
base installation, and Windows machine. It is not a clean-repository copy or
a guarantee of compatibility on every platform. No existing environment,
notebook, or source file is to be deleted. Do not copy installed packages from
`.venv` or enable access to system packages.

Deliver the task in stages: first review creation and baseline inspection,
then explain dependency installation and execution. Do not advance past the
first-stage outputs or a reported error without discussing them.

## Stage 1 — Create And Inspect

Run from `project-materials/exercises/workspaces/m01-reservations/` in
PowerShell or Command Prompt (CMD). Inspection at assignment confirms that
`.venv-repro` does not exist. If it already exists when resuming, report that
instead of reusing or deleting it and calling it fresh.

Create the second environment:

```console
py -V:3.15 -m venv .venv-repro
```

This creates local environment files. Default venv creation isolates installed
packages from the base installation; it also creates a Git ignore file in the
environment on this Python version. The `.venv-repro` name is a chosen directory
name, not a special Python keyword. Activation and changing the VS Code
interpreter are not required for these explicit-path commands.

Inspect its Python version and interpreter path:

```console
.\.venv-repro\Scripts\python.exe --version
```

```console
.\.venv-repro\Scripts\python.exe -c "import sys; print(sys.executable)"
```

Expect Python 3.15.2 and a path ending in
`m01-reservations\.venv-repro\Scripts\python.exe`.

Inspect its installed dependency inventory before installing exercise packages:

```console
.\.venv-repro\Scripts\python.exe -m pip freeze
```

For a normally created fresh environment here, expect no package lines. This
does not mean pip is absent: freeze omits pip by default on Python 3.12 and later.
Pytest and notebook dependencies should not already be installed in this
environment. If output is unexpected, retain it for diagnosis.

Send the creation result and the three inspection outputs; explicitly report
an empty freeze result. Stop here for review before installing dependencies.
The shared commands are in
[COMMANDS.md](../../COMMANDS.md#create-and-inspect-a-reproduction-environment).

## Stage 2 — Install And Verify

Stage 1 has been reviewed from learner output: Python 3.15.2, the intended
`.venv-repro` executable path, and an empty pre-install freeze. Continue from
the same exercise directory. Run each command separately; if an installation
fails, retain its error and discuss it before continuing.

Install the pip version recorded in the operational setup notes:

```console
.\.venv-repro\Scripts\python.exe -m pip install pip==26.3
```

Confirm pip 26.3 and a path inside `.venv-repro`:

```console
.\.venv-repro\Scripts\python.exe -m pip --version
```

Install the recorded package requirements:

```console
.\.venv-repro\Scripts\python.exe -m pip install -r requirements-dev.txt
```

Both install commands change only the selected environment and may download
packages. `-r` reads the file; `==` selects the recorded version. Use the pinned
file rather than independently upgrading packages or changing requirements to
conceal an installation difference.

Inspect the installed inventory and compare names and versions against
`requirements-dev.txt`; pip itself is omitted by default:

```console
.\.venv-repro\Scripts\python.exe -m pip freeze
```

After successful installation, run the unchanged example and tests through
the reproduction interpreter:

```console
.\.venv-repro\Scripts\python.exe reservations.py
```

```console
.\.venv-repro\Scripts\python.exe -m pytest
```

Expect the example to print `50` and the test summary to report exactly
`3 passed`. Send the installation completion/error messages, pip-version output,
freeze output and any comparison differences, and both execution results.
A passing run verifies these exercise cases; notebook execution is not assessed.
A failure is diagnostic evidence, not permission to claim reproduction or
alter expected results.

Review actual learner output and explanation of interpreter selection and
version-controlled files against M01 acceptance. Existing evidence may support
that explanation; do not repeat already resolved questions. Preserve distinctions
between learner implementation, supplied reference code, and mentor-authored
documentation. Creating an environment alone does not complete this task or M01.
No new environment or reproduction evidence is claimed at assignment.

Sources: [venv](https://docs.python.org/3/library/venv.html),
[pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/).
