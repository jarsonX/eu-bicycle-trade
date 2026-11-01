# M00 Part 8 Understanding Feedback

Reviewed: 2026-11-01 (Europe/Warsaw). Evidence: the learner's chat answers to
[m00-08-type-hints-and-runtime-validation.md](../lectures/m00-08-type-hints-and-runtime-validation.md).

The learner correctly identified the mismatch between the declared `int` return
and actual `str` return. He correctly explained that plain Python annotations
do not enforce runtime validation or reject that value merely because it
conflicts with the annotation.

For the unit question, he correctly explained that both hour and minute values
can satisfy `list[int]`. He proposed normalizing the documented hour values to
the already required minutes before using them with the minute source.

He also correctly challenged the request to "establish" additional facts:
the prompt had already supplied both source units and the target contract.
No additional hidden decision or investigation was required to answer the
question as stated. The mentor acknowledges that this wording was redundant;
do not invent missing requirements or assess the learner against unstated
conditions. Preserve source/contract verification as a general principle while
recognizing that those facts were given in this particular question.

Status: both part 8 conceptual checks met. No extra check is needed. No code
execution, type-checker run, independent implementation, or M00 completion is
inferred. Continue to part 9 on exceptions, failure policy, logging, and network
boundaries.
