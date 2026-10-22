# M00 Starting-Point Feedback

Reviewed: 2026-10-22. Evidence: the learner's answers in chat to
[m00-starting-point.md](m00-starting-point.md). This is a reasoning review;
the learner did not report running code or Git commands.

## Python

The learner correctly predicted `135` and traced the running totals as
`0 + 30`, `30 + 60`, and `90 + 45`. He identified initialization, iteration,
and returning a value correctly.

Refinement: `total` is an accumulator, holding the running result throughout
the loop, not only a starting point. A Python function that reaches its end
without executing `return` returns `None` implicitly. Functions without an
explicit return value can be useful for effects such as printing, writing a file,
or updating an external system. Printing a result is different from returning it
to the caller. These refinements are explained in chat; understanding remains
to be checked in later work.

## SQL

The learner supplied:

```sql
SELECT room, SUM(duration_minutes) AS total_minutes
FROM reservations
GROUP BY room
```

He correctly expected A = 90 minutes and B = 45 minutes. Grouping and aggregation
are demonstrated on this disclosed sample. Without `ORDER BY`, result order is
not guaranteed; the row order in his answer is not an error.

## Git

The learner correctly identified `git status` and explicitly stated uncertainty
about inspecting changed lines. Introduced `git diff` for unstaged changes to
tracked files, `git diff -- path/to/file.py` for one file, and `git diff --staged`
for staged changes. These commands have been explained, not demonstrated by
the learner.

## Teaching Decision

Proceed with the M00 lecture using the reservation example. Build on demonstrated
loop/function and SQL aggregation reasoning. Explain Python return values versus
effects and Git change inspection; revisit these in M01. Other Python, pandas,
environment, SQL join, and Git skills remain unassessed. The learner did not
provide a prior-preparation statement; no previous completion is inferred.
This diagnosis does not complete M00 or establish M01/M02 readiness.
