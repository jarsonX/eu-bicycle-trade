# M01 Step 10 — Review Files And Changes In Git

Prerequisite: accepted configuration and learner execution under
[m01-09-pytest-configuration.md](m01-09-pytest-configuration.md).
Run the commands below from the repository root, `eu-bicycle-trade`,
in PowerShell or Command Prompt (CMD).

## Purpose And Current Evidence

Review file selection and the meaning of an actual change before staging.
The exercise workspace currently contains source, tests, configuration,
requirements, setup instructions, a sandbox notebook, and generated caches.
Its files are currently untracked. The `.venv` tracking/ignore discussion is
already complete and does not need to be repeated.

Python creates `.pyc` files containing compiled bytecode under `__pycache__`;
these are generated execution artifacts, not manually authored source. They can
be regenerated from the source. Current Git inspection lists two such files
as untracked and not ignored. They should be excluded from version control.
Do not use a blanket rule that also hides the exercise's Python source files.

The contents and intended role of `dev_sandbox.ipynb` have not been reviewed.
Explain whether it is useful work to retain or a disposable scratchpad; its
extension alone does not determine whether it belongs in Git. Do not delete it
as part of this review.

## First Review

1. List workspace changes with individual untracked paths:

   ```console
   git status --short --untracked-files=all -- project-materials/exercises/workspaces/m01-reservations/
   ```

   `--untracked-files=all` expands untracked directories into file entries.
   `--` separates options from the path limiting the inspection. `??` marks an
   untracked file. In the two-column status, ` M` marks an unstaged modification
   to a tracked file; a staged modification uses `M ` instead.
   Normally ignored files are omitted; they still exist on disk.

2. Read a small actual patch in a tracked task document:

   ```console
   git diff -- project-materials/exercises/tasks/m01-02-virtual-environment.md
   ```

   A diff is a comparison showing changed lines. Here it compares the working
   file with its indexed version. Content lines beginning with `+` are additions;
   those beginning with `-` are removals. The `---` and `+++` lines identify the
   compared files, not deleted or added document text. The `@@` header gives
   the line ranges for a changed block. If a pager opens, press `q` to leave it.

3. Open the workspace's untracked text files in Visual Studio Code to review
   their contents. Ordinary `git diff` does not display untracked file content;
   an empty diff for an untracked source file is not evidence of no work.
   Source and tests were already reviewed; do not rewrite them for this step.

Send both command outputs, identify the workspace files you intend to retain
in version control, explain the sandbox notebook's role, and describe the
meaning of the tracked-document change in one sentence.
The commands are inspections; staging, committing, pushing, and deletion are
not part of this task.

The shared command reference is [COMMANDS.md](../../COMMANDS.md#review-workspace-files-and-a-tracked-patch).

Proceed only after the learner's file selection, notebook role, and patch
interpretation have been discussed. Command output alone does not complete
this review. Explain diff notation before assessing it when needed.

After that discussion, create `.gitignore` in the exercise workspace, beside
`reservations.py`, and add `__pycache__/` on its own line. The trailing slash
restricts the pattern to directories; the ignore file applies to its subtree.
Keep the generated files on disk. Repeat the same path-limited status command
from the repository root. The `.pyc` entries should be omitted, `.gitignore`
should appear as a candidate, and intended source files should remain visible.
This follow-up was introduced after learner output confirmed untracked caches;
no untracking operation is required for that observed state.

In the review discussion, the learner chose not to retain `dev_sandbox.ipynb`
in version control because it is no longer needed. Add that specific filename
as a second ignore rule in the same workspace file, preserving it on disk.
The follow-up status should omit this notebook as well as generated caches.

## Completion Criterion

The learner reviews the actual inventory and patch, makes a reasoned file
selection, and subsequently adds a scoped ignore rule for generated Python
caches with mentor guidance. A follow-up status check must omit generated cache
files while retaining intended source, tests, configuration, documentation,
requirements, and the ignore file as candidates. Discuss notebook disposition
before changing it. If cache files have become tracked, inspect that state before
any index operation; ignore rules alone do not stop existing tracking.
No learner inspection, ignore-file change, or completed review is claimed at
assignment. Setup/usage documentation and fresh-environment reproduction follow.

Sources: [git status](https://git-scm.com/docs/git-status),
[git diff](https://git-scm.com/docs/git-diff),
[gitignore](https://git-scm.com/docs/gitignore).
