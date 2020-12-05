import math

def read_input_file():
  with open("./input.txt") as file: 
    for row in file:
      yield row.rstrip("\n")

def get_seat_id(b_pass):
  row = [0, 127]
  col = [0, 7]

  for char in b_pass:
    row_mid = ((row[1] - row[0]) // 2) + 1
    col_mid = ((col[1] - col[0]) // 2) + 1

    if char == "F":
      row[1] -= row_mid
    elif char == "B":
      row[0] += row_mid
    elif char == "L":
      col[1] -= col_mid
    elif char == "R":
      col[0] += col_mid

  return row[0] * 8 + col[0]

def get_my_seat():
  smallest_seat_id = 965
  highest_seat_id = 965 # from part 1
  # missing num in sequence algo for 1-x
  total = (highest_seat_id - 1 + 1) * (highest_seat_id - 1 + 2) // 2

  for line in read_input_file():
    seat_id = get_seat_id(line)
    total -= seat_id
    smallest_seat_id = min(smallest_seat_id, seat_id)

  my_seat = total - sum(x for x in range(1, smallest_seat_id))
  print(my_seat)
  return my_seat

get_my_seat()