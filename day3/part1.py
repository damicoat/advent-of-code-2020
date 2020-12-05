def read_input_file():
  with open("./input.txt") as file: 
    for row in file:
      yield row.strip()

def count_trees():
  num_trees = 0
  x_coord = 0
  for line in read_input_file():
    x_coord = x_coord % len(line)

    if line[x_coord] == "#":
      num_trees += 1
    
    x_coord += 3

  print(num_trees)
  return num_trees

count_trees()