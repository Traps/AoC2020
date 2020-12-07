def string_to_seat_id(string):
    row = string[:7].replace("F","0").replace("B","1")
    column = string[7:].replace("L","0").replace("R","1")

    return 8* int(row, base=2) + int(column, base=2)

with open("input", "r") as input_file:
    seat_strings = list(input_file)

seat_ids = list(map(string_to_seat_id, seat_strings))

open_seats = [sid for sid in range(min(seat_ids), max(seat_ids)) if sid not in seat_ids]

print(max(seat_ids))
print(min(open_seats))