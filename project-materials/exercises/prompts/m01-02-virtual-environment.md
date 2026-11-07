# M01 Step 2 — Create An Exercise Virtual Environment

Assigned: 2026-11-07 (Europe/Warsaw).
Prerequisite: learner-supplied output confirms Python 3.15.2 is available;
see [m01-01-interpreter-discovery.md](m01-01-interpreter-discovery.md).

## Purpose

A virtual environment provides a separate package installation location for
this exercise, using the installed Python as its base. Its directory will be
`.venv` inside `project-materials/exercises/workspaces/m01-reservations/`. Learner code
belongs outside `.venv`. The environment is generated locally and must not be
committed to Git; ignore behavior will be checked before staging any files.

The mentor checked the official [venv documentation](https://docs.python.org/3.15/library/venv.html).
Current [pytest maintainer metadata](https://pypi.org/project/pytest/) explicitly
lists Python 3.15 support. This permits proceeding with the available interpreter;
local package installation and tests remain unverified. No final bicycle-project
dependency stack is selected by this exercise choice.

## Task And Command Explanation

Create the directory `project-materials/exercises/workspaces/m01-reservations/` yourself,
using your editor, File Explorer, or PowerShell. Do not create another Git
repository. Then enter that directory in PowerShell:

```powershell
Set-Location 'C:\Users\jaros\OneDrive\_Tech\_git_repos\eu-bicycle-trade\project-materials\exercises\workspaces\m01-reservations'
```

`Set-Location` changes the current directory. The following destination is
relative to that directory, which is why location matters.

```powershell
py -V:3.15 -m venv .venv
```

`-V:3.15` chooses the installed Python 3.15 interpreter. `-m` runs a Python
module as a program; a module is a named unit of Python code. `venv` is the
built-in environment-creation module. `.venv` is the target directory name,
not another package or version. The command creates local environment files.

Verify the environment interpreter directly:

```powershell
.\.venv\Scripts\python.exe --version
```

The explicit relative path selects the executable inside the exercise
environment. Activation is optional for this invocation; it will be explained
later. `--version` prints the version and exits. The version is expected to
match the base interpreter, 3.15.2; a mismatch is a finding to investigate.

Send the final command's output or any error and name your intended editor.
If something fails, retain the full error rather than repeating changes blindly.
No package installation, function implementation, or test is assigned yet.

## Completion Criterion And Evidence Limits

The learner reports the exercise-directory creation and supplies the direct
environment-interpreter version output. These commands are mentor-provided
setup scaffolding; execution alone does not establish independent design or
coding mastery. Later M01 tasks require learner-written code/tests, reasoning,
setup notes, Git review, and fresh-environment reproduction under
[LEARNING.md](../../../project-guidance/LEARNING.md#m01--environment-and-repository).

This document is a prompt, not evidence that an environment was created.
