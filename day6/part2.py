def read_input_file():
  with open("./input.txt") as file: 
    for row in file:
      yield row.rstrip("\n")

def sum_group_everyone_yes():
  total = 0
  first_in_group = True
  yes_per_group = set()

  for line in read_input_file():
    # group delimiter
    if line == "":
      total += len(yes_per_group)
      first_in_group = True
      yes_per_group = set()
    else:
      intersection = set()

      for char in line:
        if char in yes_per_group or first_in_group:
          intersection.add(char)
        
      yes_per_group = intersection
      first_in_group = False

  # no newline at EOF means checking final record
  total += len(yes_per_group)
  print(total)
  return total

sum_group_everyone_yes()