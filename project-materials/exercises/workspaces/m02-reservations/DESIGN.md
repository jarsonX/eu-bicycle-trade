# Reservation Processing Design

The input contract is defined in
[m02-01-responsibilities-and-interfaces.md](../../tasks/m02-01-responsibilities-and-interfaces.md#input-and-contract).
All records describe reservations for one fictional day. The whole export is
validated before a requested-room total is accepted.

## Responsibilities And Interfaces

| Part | Responsibility | Input | Result and effects |
| --- | --- | --- | --- |
| Configuration object | Group the data-file path, encoding, and requested room. | Values selected for the run. | Configuration values available to the coordinating code. The concrete representation will be chosen during orchestration. |
| `load_reservation` | Read and parse the complete local export. | `input_path` as `Path`, `encoding` as `str`. | `list[Reservation]` whose business rules still require validation. Reads a file. File-access and parsing failures propagate. |
| `validate_reservations` | Check the complete export against the business rules. | The loaded reservations as `list[Reservation]`. | Successful validation returns `None`. Invalid data raises `ValueError` with a useful explanation. Input records are preserved. |
| `total_minutes_for_room` | Sum booked minutes for the requested room. | Validated reservations and `requested_room` as `str`. | An `int` total in minutes. Empty input and no matching reservations yield zero. Input records are preserved. |
| Main-guard code | Coordinate the steps and print the result. | Configuration and the results of preceding steps. | A successful report is printed after validation and calculation succeed. |

The validation rules cover unique reservation identifiers, the exact minute-unit
label, strictly positive durations, and nonblank room labels, under the input
contract's guaranteed field structure and basic types.

## Execution Order

Configure the run, load the complete export, validate it, calculate the requested
room's booked minutes, and print the result. A failure interrupts this sequence.

## Implementation Order

Begin with the record type and loader in
[mixed_reservations.py](mixed_reservations.py), under
[m02-02-load-reservations.md](../../tasks/m02-02-load-reservations.md).
Continue with validation under
[m02-03-validate-reservations.md](../../tasks/m02-03-validate-reservations.md).
Calculation and the configuration object follow in separate steps.
