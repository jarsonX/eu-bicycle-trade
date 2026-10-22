# M00 Part 2 Understanding Feedback

Reviewed: 2026-10-22. Source: the learner's chat responses to
[m00-02-data-meaning-and-contracts.md](../lectures/m00-02-data-meaning-and-contracts.md).

## Demonstrated Understanding

The learner correctly rejected deduplicating reservation records by room and
explained that many reservations can belong to one room. He identified
`reservation_id` as the expected key and related identification to grain.

He correctly declined to report an exact complete total when one day is missing.
He independently inferred the valid lower bound of 90 minutes, under the
example's nonnegative-duration and correct-observation assumptions.

## Refinements Delivered

His description of grain as room plus reservation duration needs correction:
one row represents one individual reservation; room and duration are attributes
and can both repeat across distinct reservations. Room can be part of a key at
a different grain, so its irrelevance to duplicate detection is specific to
the original reservation table.

He assumed uniqueness would be enforced by the table. That is conditional on
an actual active constraint; CSV input does not provide it. Repeated keys may
also arise from combined exports or joins. Expected keys and actual enforcement
are distinguished in the lecture supplement. Conflicting repeated IDs need not
be identical duplicate rows.

He proposed mean/mode filling with a larger sample. This was an extension beyond
the question, not required for the original answer. Sample size alone does not
justify imputation. Feedback defines imputation and mode and explains missingness
patterns, comparable observations, agreed policy, and labelling estimated totals.
The current example retains partial/unknown totals rather than silently imputing.

The lecture file preserves these explanations. The original core answers were
substantially correct. The follow-up review below establishes the demonstrated
understanding; no implementation or main-project readiness is inferred.

## Targeted Follow-Up

1. Two confirmed distinct reservations have rows `(101, A, 30)` and
   `(102, A, 30)` in columns `reservation_id`, `room`, and `duration_minutes`.
   Are these duplicates? What does one row represent?
2. You have 1000 days of data, but missing daily totals tend to occur on
   unusually busy days. Does the number of days alone justify replacing gaps
   with the global observed mean? Would the replacement be an observation or
   an estimate? Explain briefly.

## Follow-Up Review

The learner correctly stated that the two distinct reservation IDs are not
duplicates and that one row represents one reservation. He correctly explained
that filling an unknown value produces an estimate regardless of the analysis
purpose, and distinguished that from recovering an actual observation from
another system. He recognized that differences between days can undermine a
global mean replacement.

Clarification delivered: seasonality requires a recurring time pattern, not
merely differences between days. In the disclosed failure example, missingness
associated with unusually busy days is the direct reason the observed mean
may be unrepresentative; a seasonal pattern is not required.

Recovering an observation from another system also requires matching the same
reservation/day, definition, unit, scope, and relevant revision, with the source
recorded. This extends the learner's valid provenance distinction rather than
rejecting it. The grain and estimation follow-up checks are met. Uniqueness
enforcement was explained previously but not independently re-demonstrated.
Proceed to M00 provenance, snapshots, and reproducibility.
