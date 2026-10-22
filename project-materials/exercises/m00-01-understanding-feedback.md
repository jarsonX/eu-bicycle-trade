# M00 Part 1 Understanding Feedback

Reviewed: 2026-10-22. Source: the learner's answers in chat to
[m00-01-responsibilities-and-interfaces.md](../lectures/m00-01-responsibilities-and-interfaces.md).

The learner correctly identified input acquisition as the responsibility affected
by replacing CSV input with database input. He explained that preserving the
agreed list representation allows downstream code to remain unchanged. This
demonstrates reasoning about separation of responsibilities and interface stability.
Clarification supplied in feedback: the agreement covers units, meaning, and
validation guarantees as well as the list's shape; a separate file per
responsibility is an implementation choice, not a requirement.

The learner correctly assigned negative-duration rejection to validation and
required the process to stop with a useful error rather than report a successful
total. He proposed a user-facing explanation. Feedback refines the wording to
"duration cannot be negative" and recommends identifying the field and record
in this fictional, non-sensitive example. Raising/handling exceptions and the
coordinator's response will be taught later; no implementation ability is inferred.

Both conceptual checks are met for this lecture part. This is not a pass for
M00 or evidence of independent M01/M02 exercise readiness. No code was submitted
or executed for this check.
