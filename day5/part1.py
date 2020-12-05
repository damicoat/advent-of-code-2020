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

    if char == "F": # lower
      row[1] -= row_mid
    elif char == "B":
      row[0] += row_mid
    elif char == "L":
      col[1] -= col_mid
    elif char == "R":
      col[0] += col_mid

  return row[0] * 8 + col[0]

def get_highest_seat_id():
  highest_seat_id = 0
  for line in read_input_file():
    seat_id = get_seat_id(line)
    highest_seat_id = max(highest_seat_id, seat_id)

  print(highest_seat_id)
  return highest_seat_id

get_highest_seat_id()