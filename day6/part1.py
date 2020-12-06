def read_input_file():
  with open("./input.txt") as file: 
    for row in file:
      yield row.rstrip("\n")

def sum_group_yes():
  total = 0
  yes_per_group = set()

  for line in read_input_file():
    if line == "":
      total += len(yes_per_group)
      yes_per_group = set()
    else:
      # build up records from rows
      qs = [char for char in line]
      for q in qs:
        yes_per_group.add(q)

  # no newline at EOF means checking final record
  total += len(yes_per_group)
  print(total)
  return total

sum_group_yes()