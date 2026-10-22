# M00 Part 2 — Data Meaning And Contracts

This continues the M00 theory using fictional meeting-room data. It requires
the responsibilities and interface concepts in
[m00-01-responsibilities-and-interfaces.md](m00-01-responsibilities-and-interfaces.md).

## Contents

- [Row Meaning And Grain](#row-meaning-and-grain)
- [Keys And Duplicate Records](#keys-and-duplicate-records)
- [Units And Comparable Aggregation](#units-and-comparable-aggregation)
- [Missing Is Different From Zero](#missing-is-different-from-zero)
- [A Data Contract](#a-data-contract)
- [Understanding Check](#understanding-check)

## Row Meaning And Grain

Grain is the precise meaning of one row. In the reservation example, one row is
one reservation, not one room and not a daily total. For this sample all three
reservations are on the same day, each ID is globally unique, the durations are
positive integer minutes, and there are no missing values or overlaps.

| reservation_id | room | duration_minutes |
| --- | --- | --- |
| 1 | A | 30 |
| 2 | A | 60 |
| 3 | B | 45 |

Room A appears twice because it has two distinct reservations. Grouping by room
and summing durations produces A = 90 and B = 45 minutes. The result has a new
grain: one row per room for the sample day. It no longer represents individual
reservations. Before manipulating a table, describe what one row means; the
same columns or numerical types do not guarantee the same meaning.

The grain is one individual reservation, not the combination of room and
duration. Two distinct reservations can have the same room and the same
duration. Those attributes describe the reservations but do not necessarily
identify them.

## Keys And Duplicate Records

A key is a field or combination of fields that identifies one row uniquely at
the agreed grain. Here `reservation_id` is the key. `room` is not a key for the
reservation table, because several valid reservations can use the same room.
For a table of daily room totals covering many days, the pair `(date, room)`
can serve as a composite key: a key made from more than one field.

If reservation 2 is accidentally received twice, a naive sum becomes
30 + 60 + 60 + 45 = 195 instead of 135. Rejecting repeated `reservation_id`
values detects the problem. Removing duplicate rooms would instead remove valid
reservations. Arbitrarily keeping one of two conflicting rows with the same ID
could also discard a correction or conceal an error. This example's rule is to
stop and clarify duplicate reservation IDs rather than repair them silently.

Declaring a field to be the expected key is different from enforcing that
requirement. An active primary-key or appropriate uniqueness constraint in a
database prevents duplicate key values in the constrained table. A CSV file
does not enforce such a constraint, and combining overlapping exports or joining
tables can repeat an otherwise valid source ID. Validate the actual data at the
boundary. Repeated IDs violate our expected key; if the other fields differ,
they are conflicting records rather than identical full-row duplicates.
Room remains relevant in other grains, such as the `(date, room)` daily key.

## Units And Comparable Aggregation

A unit states what a numerical value measures. Two hours and 30 minutes cannot
be added as `2 + 30` and labelled minutes. With known units, convert the two
hours to 120 minutes, then add to obtain 150 minutes. Conversion is a justified,
documented normalization step. If the unit is unknown, guessing a conversion is
not valid normalization. The downstream contract should define one unit.

Aggregation combines detailed observations into summaries, such as `SUM` in SQL.
Its validity depends on the measure and matching meaning, units, and periods.
Do not combine detail rows with summaries of those same rows: the original
durations total 135, and the room totals also total 135; adding both sets yields
270 by counting every reservation twice. Similarly, averaging room averages
without considering reservation counts does not necessarily yield the overall
mean reservation duration. First define the question and the records that
contribute to its answer; then choose the operation.

## Missing Is Different From Zero

Consider a separate fictional daily summary for room A. Its grain is one row per
date and room. Under this summary's rules, a confirmed day without bookings has
zero reserved minutes. A failed daily delivery has an unknown value, shown here
as "missing" for readability rather than as an executable data format.

| date | room | reserved_minutes | meaning |
| --- | --- | --- | --- |
| 2026-10-19 | A | 90 | confirmed total |
| 2026-10-20 | A | missing | daily delivery failed |
| 2026-10-21 | A | 0 | confirmed no reservations |

Zero is known information. Missing means that the relevant information is not
available. The two known days sum to 90 minutes, but that does not establish a
complete three-day total. Label it as a partial sum covering two of three days,
or leave the requested complete total unavailable, according to the agreed
reporting rules. Replacing the missing value with zero invents an observation.

Because daily durations are nonnegative and the two observed daily totals are
assumed correct, the complete three-day total is at least 90 minutes. This is
a lower bound, not an exact total. It is a valid inference under the disclosed
assumptions, even though the exact total remains unknown.

Imputation means replacing a missing observation with an estimated value. The
mean is the sum of observed values divided by their count; the mode is the most
frequent observed value, and it need not be unique. More observations alone do
not justify either replacement. The reason for missingness, comparability of
days, purpose of analysis, and agreed rules matter. For example, if failures
occur especially on unusually busy days, the observed days may underrepresent
busy days even in a large dataset. A global mean may then underestimate the
missing values. An imputed total must remain labelled as an estimate with its
assumptions; it is not a recovered observation. The current daily example's
rules do not authorize silently filling missing values.

This does not change the earlier positive-duration rule for individual
reservations. A zero-minute reservation is invalid under that rule; a zero
daily total is valid when no reservations occurred. The same number can be
valid or invalid depending on the field's meaning and grain. An absent row is
another possible sign of missing delivery; absence alone does not prove zero.

## A Data Contract

A data contract is an explicit agreement describing the structure, meaning,
quality requirements, and handling rules for data exchanged between parts of a
process. A schema describes structural elements such as field names and types;
the contract adds the semantic and quality rules needed to use them correctly.

For our original complete reservation sample, the contract requires one row per
reservation; the fields `reservation_id`, `room`, and `duration_minutes`; a
unique integer reservation ID; a nonempty room identifier; and a positive integer
duration in minutes. Missing required values, duplicate IDs, unknown or wrong
units, and nonpositive durations stop processing before a successful total is
reported. That is the policy for this example, not a universal rule for every
dataset. The separate daily-summary example permits missing observations but
requires incomplete results to be labelled or withheld.

Validation implements checks against that agreement. A description alone does
not enforce it, while checks without a stated agreement can enforce the wrong
assumptions. Some facts, such as the actual unit or whether all reservations
were exported, require reliable source evidence; plausible numbers alone cannot
prove them. A contract makes assumptions explicit, but cannot manufacture
evidence that the source satisfies them.

## Understanding Check

1. In the original table, room A has reservations 1 and 2. Someone proposes
   rejecting any repeated `room` value as a duplicate. Is that correct? Explain
   using the table's grain and key.
2. In the daily summary, the known values are 90 and 0 minutes, while one day is
   missing. Can the report state "the complete three-day total is 90 minutes"?
   Explain what it can honestly report and why.

Answer in your own words. This check concerns M00 theory and does not replace
the independent exercises.
