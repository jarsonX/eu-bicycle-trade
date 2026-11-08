# M01 Step 6 — Record Dependencies And Setup Notes

Prerequisite: successful learner installation and version inspection under
[m01-05-pytest-installation.md](m01-05-pytest-installation.md).

Owner override: after creating `requirements-dev.txt`, the learner explicitly
asked the mentor to write `SETUP.md`. That request supersedes learner authorship
of setup notes in the original task below. The mentor created
[SETUP.md](../workspaces/m01-reservations/SETUP.md); the learner-created
[requirements-dev.txt](../workspaces/m01-reservations/requirements-dev.txt)
matches the installation log. This is assisted documentation, not evidence of
independent setup-note writing or verified fresh-environment reproduction.

## Purpose

The exercise environment is generated locally and excluded from Git. Record
the packages and setup steps needed to recreate it. A dependency inventory
lists installed package versions; `name==version` requests an exact version.
Dependencies installed for another package are indirect dependencies. Record
them too for this small Windows exercise rather than pinning only pytest.

`pip freeze` prints installed packages in requirements format; on Python 3.15,
pip itself is normally omitted. Keep Python/pip versions separately in setup
notes. An inventory is not a complete environment definition or a substitute
for the later fresh-environment check.

## Task

In the terminal using the already verified exercise environment, run:

```console
python -m pip freeze
```

This displays the inventory without creating files or changing installed
packages. The working directory may remain the repository root.

Keep these files inside
`project-materials/exercises/workspaces/m01-reservations/`, outside `.venv`:

1. `requirements-dev.txt`: copy the actual freeze output as plain text, without
   terminal prompts or Markdown fences. Keep all displayed package/version lines.
2. `SETUP.md`: under the owner's override, the mentor writes English notes
   recording Python 3.15.2, pip 26.3,
   the location of the exercise directory, the explained environment-creation
   command, the dependency-file installation command, and the pytest-version
   check. State where each command runs and how the exercise interpreter is
   selected. Keep setup instructions operational; record fresh-environment
   verification status in [PROGRESS.md](../../PROGRESS.md).

Both files use UTF-8. Commands and their meanings are in the
shared [COMMANDS.md](../../COMMANDS.md#packages-and-test-tools).
Do not install packages again or create a second environment for this step.

The future recreation command, run from the exercise directory with the intended
interpreter selected, is:

```console
python -m pip install -r requirements-dev.txt
```

`-r` reads package requirements from that file. Recording the file now and
installing from it later are separate operations. This command is for the notes;
fresh-environment execution is assigned after the function/test task.

## Completion Criterion

Under the recorded owner override, the learner creates the requirements file
and the mentor authors the setup notes. The requirements content must match
the observed inventory; setup instructions must describe requirements, commands,
and expected behavior. Record actual verification results separately in
[PROGRESS.md](../../PROGRESS.md). After review, assign
the learner's function/test task. No practical coding mastery or completed M01
is inferred from copying package output.

Sources: [pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/),
[Repeatable installations](https://pip.pypa.io/en/stable/topics/repeatable-installs/).
