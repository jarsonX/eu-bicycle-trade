# M00 Part 7 — Charts And Interpretation

This follows [m00-06-joins-and-cardinality.md](m00-06-joins-and-cardinality.md).
It uses fictional meeting-room data and remains M00 theory. The pandas example
was checked against official documentation, not executed. The conversation
visual is a separate labelled illustration in
`visuals/reserved-minutes.html`; it is not an output of an executed pandas pipeline.
No project dependencies were installed or selected.

## Contents

- [Choose The Question And Measure](#choose-the-question-and-measure)
- [A Basic Chart In pandas](#a-basic-chart-in-pandas)
- [Axes, Scope, And Missing Values](#axes-scope-and-missing-values)
- [Totals And Denominators](#totals-and-denominators)
- [Observations And Hypotheses](#observations-and-hypotheses)
- [Understanding Check](#understanding-check)
- [References](#references)

## Choose The Question And Measure

The original sample has three distinct reservations for one day, labelled D: A for 30
minutes, A for 60 minutes, and B for 45 minutes. Assume complete delivery,
positive integer minute durations, nonmissing room identifiers, and no overlaps.
Use these original records, not the duplicated join result or the filtered
subset from the preceding checks.

The question is: how much time was reserved in each room on this sample day?
The complete totals are A = 90 and B = 45 minutes. After aggregation, one row
represents one room for the day. A bar chart compares discrete categories by
bar length on a shared numerical scale. A line chart is useful for a sequence
such as daily reserved time; the order and spacing of time are meaningful.
Drawing a line between room A and room B would suggest continuity that these
category labels do not have.

## A Basic Chart In pandas

Using the complete `reservations` DataFrame introduced in part 5:

```python
room_totals = reservations.groupby("room", as_index=False)["duration_minutes"].sum()

ax = room_totals.plot.bar(
    x="room",
    y="duration_minutes",
    legend=False,
    rot=0,
    title="Reserved time by room — sample day",
)
ax.set_ylabel("Reserved time (minutes)")
ax.set_ylim(bottom=0)
```

`plot.bar()` creates a vertical bar chart; `x` supplies the categories and `y`
the numerical measure. It uses the already calculated rows rather than proving
their quality or business meaning. `legend=False` suppresses the redundant
single-series legend, and `rot=0` keeps category labels unrotated. With the
usual Matplotlib plotting backend, the returned `ax` is an Axes object: the
plotting region with data marks, axes, labels, and title. Matplotlib is a Python
plotting library required by that backend. This is code to understand now;
environment setup remains in M01.

`set_ylabel()` gives the vertical axis a readable measure and unit;
`set_ylim(bottom=0)` starts its scale at zero. Creating a plot object is separate
from saving an image file. The inline teaching illustration is not evidence
that the learner or agent ran this pandas example.

## Axes, Scope, And Missing Values

For a bar chart, length conveys magnitude, so a zero baseline preserves the
visual ratio of nonnegative values. If bars for 90 and 45 are truncated at 40,
their visible lengths become 50 and 5: a 10:1 visual ratio for values that are
actually 2:1. This is a bar-chart concern; a line chart may use a narrower
clearly labelled range to show changes without using bar length as the encoding.

Label the measure, unit, time scope, and relevant selection. A chart of only
reservations lasting at least 45 minutes must disclose that filter. If the
data is partial, label that limitation or withhold the complete total under
the reporting contract. Missing days are unknown, not confirmed zero days;
do not draw a zero observation or an uninterrupted measured series across a
missing period without explicitly defining and labelling the treatment.
Reports should also identify the snapshot supporting the plotted values.

## Totals And Denominators

Reserved minutes are an absolute total. The proportion of available time that
was reserved requires a denominator: the available room minutes over the same
period and scope. Compute `reserved_minutes / available_minutes * 100` only
when availability is known, positive, and comparable. For example, 60 reserved
minutes out of 240 available minutes is 25%.

More reserved minutes do not necessarily imply a larger reserved share when
rooms have different availability. This measure is based on reservations; it
does not establish actual presence or use during the booked time. Missing or
zero availability prevents the intended percentage calculation and needs an
explicit reason rather than an invented percentage. Overlapping reservations
would also require a different definition or validation; the sample excludes them.

## Observations And Hypotheses

An observation is a statement supported directly by the disclosed measurements,
such as a larger reserved-minute total for A on this day. A hypothesis proposes
an explanation that needs additional evidence, such as better room equipment
causing people to choose A. The chart has no equipment, preference, or causal
information and covers only one sample day.

Empirical evidence can support or weaken a hypothesis, and the conclusion may
remain unresolved. A survey of booking users is a useful starting point for
learning their reported reasons, but those reports do not by themselves prove
the independent causal effect of equipment. Equipment, proximity to coffee,
room availability, and meeting needs may all contribute. Finding evidence for
one factor does not automatically rule out another. State what was actually
measured, what the respondents reported, and which causal interpretation still
requires stronger evidence.

A useful report distinguishes the measured finding, its scope, the limitations,
and questions for further investigation. A polished chart can present erroneous
join totals just as convincingly as correct totals. Trace the plotted numbers
back to the validated data and manual calculation, rather than treating visual
polish as evidence of correctness.

## Understanding Check

The question is about fictional day D only. Every value in the table below
refers to that same day and the same room. Reserved time is the complete
sum of the original reservations described above. The bookable window is the
total time offered for booking that day, including both booked and unbooked
time; it is not the remaining free time. No 24-hour or office-hours assumption
is needed beyond the supplied window. Reservations fit within those windows
and do not overlap; all values use minutes.

| Room | Reserved minutes on day D | Total bookable minutes on day D |
| --- | --- | --- |
| A | 90 | 480 |
| B | 45 | 60 |

This restatement repairs the chat prompt's indirect reference to earlier data.
The mentor subsequently supplied the numerical substitutions in chat; question
1 is therefore assisted material rather than a fresh independent check.

1. What percentage of available time was reserved for each room? Which room
   has the larger reserved share, and does that match the ordering of totals?
2. Someone states: "A had more reserved minutes because it has better
   equipment." Is that an observation supported by this chart or a hypothesis?
   What additional evidence would you want before accepting the explanation?

Use reasoning and small calculations, without installing or running anything.

## References

Consulted on 2026-10-31. Examples and manually derived numerical explanations
are original teaching material; no project dependency version is selected.

- [DataFrame.plot.bar](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html)
- [Axes.set_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html)
- [Axes.set_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html)
