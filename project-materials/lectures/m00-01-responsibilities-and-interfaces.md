# M00 Part 1 — Responsibilities And Interfaces

This lecture uses fictional meeting-room reservations, not project data.
It begins the M00 introduction; later parts still need to cover the remaining
topics required by [LEARNING.md](../../project-guidance/LEARNING.md).

## From A Correct Sum To A Trustworthy Process

In the diagnostic, one row represented one reservation, identified by a unique
`reservation_id`. The three durations were 30, 60, and 45 minutes, with the first
two reservations in room A and the last in room B. All belonged to the same day;
there were no missing values, duplicates, or overlaps. The total reserved time
was 135 minutes. These assumptions make the arithmetic meaningful: the same
reservation must not be counted twice and hours must not be mixed with minutes.

A correct sum is one part of an analytical process. The process must also obtain
the input, establish that it is suitable, calculate the result, and present it
with its meaning and unit. A CSV file is a text file storing tabular records,
typically with commas separating fields. Reading one involves finding the file,
interpreting its contents, and dealing with possible access or format errors.
Those problems differ from adding three numbers.

## Responsibilities And Boundaries

A responsibility is a coherent job assigned to a piece of code. Input/output
means exchanging information with the outside of a calculation, such as reading
a file or writing a report. Validation checks whether data satisfies explicitly
stated requirements. Calculation transforms suitable input into a result.
Reporting presents that result with labels, units, and relevant limits.
Orchestration coordinates these activities in the required order and responds
when a stage cannot proceed.

For the reservation example, the reader obtains the records, validation checks
the required columns and valid minute durations, a calculation totals the
durations, and reporting presents reserved time in minutes. The coordinator
connects the steps. If validation finds an invalid negative duration, this
example's rule is to stop before reporting a successful total, rather than
silently removing or replacing the value.

Keeping these responsibilities distinct helps changes stay local. If the source
changes from a CSV file to a database, obtaining the records changes. If the
calculation still receives the same validated durations in minutes, its rule
does not need to change. Likewise, changing a report from text to a chart should
not require rewriting addition. A chart here means a graphical presentation of
the same computed result, not a new definition of the measure.

## Functions, Modules, And Interfaces

A function is a named operation that can receive arguments and return a result.
A module is a unit of Python code, commonly a `.py` file, that can contain several
related functions and be imported by other code. Modularity means organizing
code into coherent parts with clear connections. It does not require a separate
file for every function. For a small example, clearly separated functions in one
file can suffice; unnecessary layers make navigation harder without improving
the calculation.

An interface is the agreement about how one part uses another: what input is
accepted, what result is produced, and what happens when the requirements cannot
be met. For the diagnostic `total_minutes(durations)`, a simple agreement is:
the caller supplies a list of already validated positive integer durations in
minutes; the function returns their total as an integer number of minutes.
An empty list returns zero, meaning the supplied list contains no reservations.
This does not prove that a missing source file represents a day with no bookings.

The agreement includes meaning and units, not just Python's value types.
`[30, 60]` in minutes and `[1, 2]` in hours are both lists of integers but cannot
be passed interchangeably to a calculation expecting minutes. Dividing the code
into functions does not by itself establish a correct interface.

## Return Values And Effects

In `total_minutes`, `total` is an accumulator: it holds the running sum after
each iteration. `return total` gives the result to the caller, which can then
compare it, divide it by 60, or include it in a report. `print(total)` writes a
representation to the output stream; it does not supply that number as the
function's return value. Replacing `return total` with `print(total)` would
therefore change the interface.

A Python function reaching the end without executing `return` returns `None`.
`None` is a special value representing the absence of a substantive result.
Such functions can still do useful work by producing effects, such as saving a
file. An effect is an observable interaction or change outside the returned
value. Separating calculation from these interactions lets us check arithmetic
without needing an actual input file or output directory. Input/output still
requires its own checks; separation does not remove that responsibility.

## Understanding Check

Answer in your own words; no installation or implementation is required.

1. The input source changes from a CSV file to a database, but the calculation
   still receives the same validated list of minute durations. Which
   responsibility changes? Should the summing function change? Explain why.
2. A source row contains a duration of `-20` minutes. Under this example's
   positive-duration requirement, which responsibility should reject it, and
   should a successful total be reported afterward?

These questions check this lecture part only. They do not replace the later
independent exercises or establish readiness for main-project work.
