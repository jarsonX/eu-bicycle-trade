# M00 Part 3 Understanding Feedback

Reviewed: 2026-10-29 (Europe/Warsaw). Source: the learner's chat responses to
[m00-03-provenance-snapshots-and-reproducibility.md](../lectures/m00-03-provenance-snapshots-and-reproducibility.md).

## Demonstrated Understanding

For question 1, the learner correctly stated that a different result after
fetching the same period again does not establish a code defect. He proposed
comparing the snapshots underlying the two reports and recognized that losing
the earlier snapshot prevents a direct comparison. This demonstrates a useful
investigation method and understanding of why inputs must be retained.

His claim that data "must" have changed is stronger than unchanged code alone
supports. Configuration or environment can also differ. The disclosed example
does involve a source correction, but that cause is not established by the
code version alone. Feedback advises comparing records by `reservation_id`
rather than row position. This clarification is saved in the lecture.

## Question 2 And Learner Clarification

In his initial answer, the learner identified environment configuration as
important and correctly declined to guarantee exact reproduction. He did not
address the original export being unavailable from the source.

The learner then explicitly explained that he had overlooked the sentence
stating that the source now provides only the corrected version. Once that
condition was noticed, he correctly recognized that the original report cannot
be reproduced from the revised export alone. His earlier answer to question 1
had already recognized the need for the historical snapshot to compare inputs.

The recorded cause is therefore a missed condition in the question, as clarified
by the learner, rather than demonstrated misunderstanding of snapshots or
reproducibility. His point about preserving the environment remains valid as
another requirement, but does not resolve the unavailable historical input.

Status: part 3 conceptual checks met based on the initial snapshot reasoning
and the explicit clarification. This does not complete all of M00 or establish
implementation or independent-exercise readiness.

## Assessment Context And Next Step

The learner explicitly clarified that the mentor's original assessment was
correct for the answer available at the time: the mentor could not have known
that he had overlooked the source-availability sentence. The later explanation
adds the cause of the omission; it does not make the original assessment unfair
or incorrect. The record retains both the incomplete initial answer and the
subsequent evidence that the concept is understood.

The learner separately objected to the near-duplicate follow-up question and
to a record that did not explain the oversight. That interaction concern is
distinct from the validity of the original answer assessment. His clarification
resolves the check without requiring him to answer the same question again.

The repeated question is withdrawn; no answer to it is required. Distinguish
an overlooked condition from a conceptual misunderstanding when reviewing
future answers, and use the learner's explanation and available reasoning as
evidence rather than automatically repeating the same check.

Next teaching step: continue M00 with environment, dependencies, configuration,
and notebook state versus modules, without repeating the part 3 check.
