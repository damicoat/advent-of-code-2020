import functools
import operator

def read_input_file():
  with open("3_input.txt") as file: 
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

# count_trees()

# part 2
def count_trees_2():
  # slopes = (right, down) 
  slopes_arr = [
    {
      'slopes': (1, 1), 
      'x': 0,
      'num': 0,
    },
    {
      'slopes': (3, 1), 
      'x': 0,
      'num': 0,
    },
    {
      'slopes': (5, 1), 
      'x': 0,
      'num': 0,
    },
    {
      'slopes': (7, 1), 
      'x': 0,
      'num': 0,
    },
    {
      'slopes': (1, 2), 
      'x': 0,
      'num': 0,
    },
  ]
  
  for i, line in enumerate(read_input_file()):
    for path_obj in slopes_arr:

      # when down slope is 2, skip odd slopes
      down_val = path_obj["slopes"][1]
      if (down_val != 1 and i % 2 != 0):
        continue

      x_coord = path_obj["x"] % len(line)
      num_trees = path_obj["num"]

      if line[x_coord] == "#":
        num_trees += 1

      x_coord += path_obj["slopes"][0]
      path_obj["x"] = x_coord
      path_obj["num"] = num_trees

  res = functools.reduce(
    operator.mul,
    [path_obj["num"] for path_obj in slopes_arr]
  )

  print(res)
  return res

count_trees_2()
  