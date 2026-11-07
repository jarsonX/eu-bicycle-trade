# M01 Step 1 — Install And Identify Python

Assigned: 2026-11-07 (Europe/Warsaw).
Prerequisite: completed M00 introduction, verified in
[PROGRESS.md](../../PROGRESS.md). The learner explicitly authorized starting M01.
Updated the same day: the learner reports that Python is not installed.
The initial request for command-discovery output is withdrawn, not failed.
The filename is retained to preserve the existing task reference.

Outcome: the learner subsequently supplied `Python 3.15.2` from both
`py --version` and `py -V:3.15 --version`; selecting 3.14 reported no matching
runtime. Interpreter availability is established from that output. The mentor
accepts 3.15 for M01, replacing the earlier 3.14 recommendation below; no second
installation is required for this exercise. Continue with
[m01-02-virtual-environment.md](m01-02-virtual-environment.md).

## Purpose And Working Agreement

The learner performs setup, writes code and tests, and explains his decisions.
The mentor explains tools and syntax, assigns small tasks with explicit criteria,
then reviews attempts and offers gradual hints. Running mentor-provided commands
alone is not evidence of independent understanding.

M01 will use a fictional meeting-room reservation exercise, separate from the
bicycle project. Later steps cover a virtual environment, dependencies,
imports/paths, minimal configuration, Git ignore/tracked files, a learner-written
function and pytest test, setup notes, diff review, and reproduction in a fresh
environment. No reservation dataset or calculation is assigned in this step.

An interpreter is the program that executes Python code. A terminal resolves
command names to programs or other commands; the name alone does not establish
which installation is used. A virtual environment provides an exercise-specific
Python environment and package location. Since Python is absent according to
the learner, we first guide installation, then verify the chosen interpreter
before creating an exercise-specific virtual environment.

## Initial Installation Guidance (Superseded By The Outcome Above)

The official Windows documentation recommends Python install manager, a tool
that installs and manages Python runtimes. The manager and the interpreter are
different components. The mentor proposes Python 3.14 for this exercise;
this does not select the final bicycle project's dependency stack.

1. Open the official [Windows downloads page](https://www.python.org/downloads/windows/),
   select Python install manager, and download its MSIX installer.
2. Open the downloaded file and choose Install. Complete its configuration
   prompts; report any unclear prompt or error before guessing at changes.
3. Open a new PowerShell window and install the proposed interpreter:

```powershell
py install 3.14
```

Here, `py` invokes the manager, `install` requests a runtime installation,
and `3.14` selects that Python release series. The exact installed patch
version must be observed, not invented. The command downloads and installs
Python on the learner's computer; the learner performs this action.

Then verify the selected interpreter:

```powershell
py -V:3.14 --version
```

`-V:3.14` explicitly selects the Python 3.14 interpreter; `--version` asks it
to print its version and exit. Send that result, or the error if installation
or verification fails. No virtual environment, package installation, or
reservation code is assigned yet.

Installation and version-selection syntax were checked against the official
[Windows documentation](https://docs.python.org/3/using/windows.html)
on 2026-11-07. Availability does not establish compatibility of every future
dependency; those choices and checks remain later work.

## Completion Criterion And Evidence Limits

This step is complete on the supplied Python 3.15.2 version output. The exact
installation procedure was not observed. Errors lead to guided troubleshooting,
not a failed conceptual assessment. This verifies interpreter availability;
environment isolation, package setup, and practical coding remain later steps.

This prompt is mentor-prepared scaffolding. No learner execution, interpreter
choice, installation, environment setup, coding, or M01 completion is established
by creating this file. Module acceptance remains in
[LEARNING.md](../../../project-guidance/LEARNING.md#m01--environment-and-repository).
