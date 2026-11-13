# ------------------------------------------------------------------
# Setup
# ------------------------------------------------------------------

import json
from pathlib import Path
from typing import TypedDict

# ------------------------------------------------------------------
# Variables
# ------------------------------------------------------------------

input_path = Path(__file__).with_name("reservations.json")
requested_room = "B"

# ------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------

class Reservation(TypedDict):
    reservation_id: int
    room: str
    duration: int
    duration_unit: str


# ------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------

def load_reservation(
        input_path: Path,
        encoding: str    
) -> list[Reservation]:
    '''Return dataset'''

    return json.loads(input_path.read_text(encoding=encoding))

# ------------------------------------------------------------------
# Output
# ------------------------------------------------------------------

if __name__ == "__main__":

    reservation_data = load_reservation(
        input_path=input_path,
        encoding="utf-8"
    )

    print(reservation_data)