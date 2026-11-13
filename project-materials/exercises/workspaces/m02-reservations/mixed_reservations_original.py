"""Deliberately mixed starting point using fictional meeting-room data."""

import json
from pathlib import Path

input_path = Path(__file__).with_name("reservations.json")
requested_room = "B"

reservations = json.loads(input_path.read_text(encoding="utf-8"))

total_minutes = 0
for reservation in reservations:
    if reservation["room"].strip() == "":
        raise ValueError("Room label must not be blank.")
    if reservation["room"] == requested_room:
        total_minutes += reservation["duration"]

print(f"Room {requested_room}: {total_minutes} booked minutes.")
