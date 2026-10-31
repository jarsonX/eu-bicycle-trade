# M00 Part 6 Understanding Feedback

Reviewed: 2026-10-31 (Europe/Warsaw). Evidence: the learner's chat answer to
[m00-06-joins-and-cardinality.md](../lectures/m00-06-joins-and-cardinality.md).

The learner correctly derived four output rows: two distinct A reservations and
two copies of B's reservation. He correctly calculated 180 minutes as
30 + 60 + 45 + 45 and identified B's reservation as the repeated record.

He correctly predicted that `validate="many_to_one"` rejects the faulty room
lookup. His explanation used "exactly one match" on the right. Refine that
wording: the check requires uniqueness of the right-side join keys; it does not
require every left key to find a match. A missing B lookup can still pass that
uniqueness check, while match coverage requires a separate check. The original
question's repeated right-side key is correctly diagnosed.

Status: the part 6 conceptual checks are met with that precision note delivered.
Do not repeat the original questions merely to test the revised wording. No
implementation or independent-exercise readiness is inferred. Continue M00 with
basic charts, reporting scope, denominators, and observations versus hypotheses.
