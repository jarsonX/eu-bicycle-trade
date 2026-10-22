# M00 Part 3 — Provenance, Snapshots, And Reproducibility

This lecture uses fictional meeting-room reservations. It follows
[m00-02-data-meaning-and-contracts.md](m00-02-data-meaning-and-contracts.md).
No real source is accessed and no project component is implemented.

## Contents

- [A Source Can Change](#a-source-can-change)
- [Provenance And Recovering Observations](#provenance-and-recovering-observations)
- [Preserving An Input Snapshot](#preserving-an-input-snapshot)
- [Manifest And Checksum](#manifest-and-checksum)
- [Reproducing A Result](#reproducing-a-result)
- [Understanding Check](#understanding-check)

## A Source Can Change

Our original export has one row per reservation, globally unique reservation
IDs, positive integer durations in minutes, and three valid reservations for
one day: reservation 1 in room A for 30 minutes, reservation 2 in room A for
60 minutes, and reservation 3 in room B for 45 minutes. Their total is 135.

In this fictional scenario, the source later corrects reservation 2 from 60 to
90 minutes. A new export for exactly the same day and rooms then totals 165.
The analysis code has not changed. Different results can be caused by revised
input, not only by a program defect. The calendar period and a source address
are insufficient to identify the exact data used for the first report.

## Provenance And Recovering Observations

Data provenance is the recorded origin and processing history of data: which
source and exact input were used, which scope was selected, and what changes
were applied before the result was produced. For example, replacing a missing
daily total with a matching actual total recovered from another system is
different from estimating it using a mean. Recovery still requires verifying
the same day or reservation, measure definition, units, scope, and relevant
revision; matching column names alone is insufficient. Record which source
provided the recovered observation and why it was considered compatible.

A terminology refinement from the previous check: seasonality means a recurring
time pattern, such as consistently different booking levels on Mondays versus
Saturdays. Differences between days do not alone establish seasonality.
Missing data concentrated on unusually busy days can bias the observed sample
without any seasonal pattern.

## Preserving An Input Snapshot

A snapshot is a preserved copy of the source input at a particular acquisition.
An immutable snapshot is retained without editing or overwriting its contents.
In our example, keep the original 135-minute export and the later corrected
165-minute export as separate versions. Preserve what the source actually
provided; normalization and corrections produce separate derived data rather
than rewriting the raw input.

Immutability here is an explicit workflow rule, not a claim that an ordinary
file becomes technically impossible to modify. Checks help detect accidental
changes. Keeping the old snapshot does not claim it remains the best current
data; it lets us explain and reproduce an earlier report.

Acquisition obtains a new input snapshot from the source. Local processing reads
an identified existing snapshot and produces results without requesting current
source data. Separating these actions means reproducing yesterday's report does
not silently replace its input with today's revision.

## Manifest And Checksum

A manifest is a record describing a snapshot so that it can be identified and
checked. In the example, record a unique snapshot ID, source/export reference,
selected day and rooms, retrieval time including timezone, file format, verified
minute unit, file location, and checksum. Describe any source revision information
actually supplied; do not invent unavailable metadata. Operational records must
not contain credentials or reusable authenticated links.

A checksum is a value calculated from a file's bytes. A cryptographic hash can
serve this purpose, providing a practical file fingerprint: calculate it again
and compare it with the recorded value to check whether the file's contents
match. It does not establish that the source was truthful, the scope correct,
or the calculation valid. A changed line ending can also change a file hash
without changing the interpreted numerical data.

The snapshot is the input itself; the manifest describes it. A manifest and
source address do not recreate a lost historical export if the source now
provides only revised data. The exact input must be preserved or retrievable as
an identified version. Numerical reproducibility is also different from having
identical output-file bytes, for example when a report includes a run timestamp.

## Reproducing A Result

Reproducibility means that another person can obtain the specified inputs and
run the documented process to obtain the same intended numerical results. This
requires the exact input snapshot, code version, configuration, and a compatible
specified environment. Configuration is the set of run choices, such as selected
rooms or the handling of incomplete days. The environment includes the Python
interpreter and installed libraries; a dependency is an external package used
by the code. Setup and precise version management will be taught separately.

Git records versions of tracked files and can identify the code used, but it
does not automatically preserve files excluded from tracking or data held in a
remote source. Saving the script alone does not preserve the whole analysis.
The report should identify its snapshot and code/configuration so its result
can be traced back. With the original snapshot and same calculation, the total
remains 135; with the corrected snapshot, it is 165. One is reproduction of the
earlier report, while the other is a report on updated input.

## Understanding Check

1. A report originally showed 135 minutes. After fetching the same day again,
   unchanged code yields 165. Does this alone prove a code defect? Explain what
   should be compared to investigate the difference.
2. You retained the code, source address, and retrieval date, but lost the original
   export. The source now offers only the corrected export. Can you guarantee
   exact reproduction of the original report? What input evidence is missing?

Answer conceptually; do not retrieve source data or write implementation code.
