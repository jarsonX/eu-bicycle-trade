# M01 Step 4 — Inspect Environment Ignore Rules And Tracking

Prerequisite: the learner's terminal resolves `python` to the exercise
environment, recorded in [PROGRESS.md](../../PROGRESS.md).

Outcome after discussion: learner-supplied output identified `.venv/.gitignore`,
line 2, pattern `*`, for the executable, and the corrected tracked-file listing
was empty. The mentor explained the rule-source output and the distinction
between ignoring, tracking, historical commits, staging, and committing. The
learner correctly answered that ignore rules do not end tracking, discussed
the remaining ambiguity, and explicitly accepted understanding before continuing.
This records assisted interpretation, not independent mastery of every command.
Continue with [m01-05-pytest-installation.md](m01-05-pytest-installation.md).

## Purpose And Scope

The `.venv` directory contains a generated Python environment. Exercise source
code and tests belong in version control; the generated environment should be
recreated from setup instructions and dependency declarations instead of stored
in Git. Those declarations will be prepared in later M01 work.

A `.gitignore` file contains patterns that exclude matching untracked paths from
normal Git status/add discovery. Ignore rules do not remove already tracked
files. Therefore inspect both exclusion rules and existing tracking.

This task uses the real local exercise directory, not a dataset. Commands are
read-only and operate within the existing repository. No ignore-rule edits,
staging, untracking, commits, package installation, or additional repository
creation is assigned. Shell: PowerShell or Command Prompt (CMD).

## Task

Run these commands one at a time from the repository root, `eu-bicycle-trade`:

```console
git status --short
```

```console
git check-ignore -v -- project-materials/exercises/workspaces/m01-reservations/.venv/Scripts/python.exe
```

```console
git ls-files -- project-materials/exercises/workspaces/m01-reservations/.venv/
```

The status command reports changes and untracked files. The ignore diagnostic
shows a matching pattern and its source; `-v` requests those details. The final
command lists tracked paths under the environment directory. Interpret empty
output as well as printed paths; an ignore diagnostic alone does not establish
the absence of tracked environment files. Command meanings and interpretation
details are collected in [COMMANDS.md](../../COMMANDS.md#git-inspection).

Send all outputs, explicitly saying when a command printed nothing. Explain:

1. What do the results establish about the environment executable's ignore rule
   and any already tracked environment files? Identify the rule source when shown.
2. Why should exercise code/tests and the generated environment be treated
   differently in version control?

Existing material edits may appear in status; identify their paths before
interpreting them as environment files. Do not assume which ignore file exists
or what rule will match. Diagnose the actual output.

## Completion Criterion

The learner supplies the observations and explains their scope. Where an
exclusion pattern is shown, consider its meaning (including negation with `!`).
Unexpected tracking or ignore behavior leads to discussion before any repair.
Only then proceed to dependency setup. Mentor-provided diagnostic commands
are scaffolding, not independently designed code or evidence of completed M01.
