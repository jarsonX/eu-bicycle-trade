from reservations import Reservation, total_minutes_for_room

# Test 1

def test_sum() -> None:
    reservations: list[Reservation] = [
        {"reservation_id": 1, "room": "A", "duration_minutes": 20},
        {"reservation_id": 2, "room": "B", "duration_minutes": 35},
        {"reservation_id": 4, "room": "B", "duration_minutes": 15},
    ]    
    result = total_minutes_for_room(reservations, "B")
    assert result == 50


# Test 2

def test_room_not_exist() -> None:
    reservations: list[Reservation] = [
        {"reservation_id": 1, "room": "A", "duration_minutes": 20},
        {"reservation_id": 2, "room": "B", "duration_minutes": 35},
        {"reservation_id": 3, "room": "A", "duration_minutes": 40},
        {"reservation_id": 4, "room": "B", "duration_minutes": 15},
    ]       
    result = total_minutes_for_room(reservations, "C")
    assert result == 0


# Test 3

def test_empty_list() -> None:
    reservations: list[Reservation] = []
    
    result = total_minutes_for_room(reservations, "A")
    assert result == 0
