# ------------------------------------------------------------------
# Setup
# ------------------------------------------------------------------
from typing import TypedDict

# ------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------
class Reservation(TypedDict):
    reservation_id: int
    room: str
    duration_minutes: int

# ------------------------------------------------------------------
# Data
# ------------------------------------------------------------------

reservations: list[Reservation] = [
    {"reservation_id": 1, "room": "A", "duration_minutes": 20},
    {"reservation_id": 2, "room": "B", "duration_minutes": 35},
    {"reservation_id": 3, "room": "A", "duration_minutes": 40},
    {"reservation_id": 4, "room": "B", "duration_minutes": 15},   
]

# ------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------

def total_minutes_for_room(
        reservations: list[Reservation],
        room: str,
) -> int:
    """Return total booked minutes for the requested room."""

    return sum(
        reservation["duration_minutes"]
        for reservation in reservations
        if reservation["room"] == room
    )

# ------------------------------------------------------------------
# Processing
# ------------------------------------------------------------------

if __name__ == "__main__":
    print(total_minutes_for_room(reservations, "B"))
    