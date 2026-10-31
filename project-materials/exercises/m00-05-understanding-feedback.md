# M00 Part 5 Understanding Feedback

Reviewed: 2026-10-31 (Europe/Warsaw). Evidence: the learner's chat answer to
[m00-05-pandas-inspection-filtering-and-grouping.md](../lectures/m00-05-pandas-inspection-filtering-and-grouping.md).

The learner correctly derived A = 60 and B = 45. He explained that the filter
excludes durations below 45 minutes, so only reservations 2 and 3 contribute.
He correctly identified grouping by room and summing the retained durations,
including why a group with one row still undergoes aggregation.

His explanation establishes the subset scope. The review makes the resulting
grain explicit: one row per room for reservations lasting at least 45 minutes
on the disclosed day. The result is not the total of all reservations in room A,
because reservation 1 has been excluded. No additional repetition of this check
is needed.

The learner explicitly clarified that "the code returns" was conversational
shorthand for assigning results to `selected` and `result`, not a claim that the
snippet displays them. Accept that shorthand in context; do not count it as a
return/display mistake. The pandas operations return objects which the
assignments bind to those names; output display is a separate action.

Status: part 5 conceptual check met. No actual code execution, installation,
or independent-exercise readiness is inferred. Continue M00 with joins and
cardinality, followed by basic charts.
