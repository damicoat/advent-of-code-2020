def read_input_file():
  with open("./input.txt") as file: 
    return [list(row.rstrip("\n")) for row in file]

def get_next_state(grid, i, j):
  if grid[i][j] == '.':
    return grid[i][j]

  num_occupied_around = get_num_occupied_around(grid, i, j)
  if grid[i][j] == 'L':
    if num_occupied_around == 0:
      return '#'
  elif grid[i][j] == '#':
    if num_occupied_around >= 4:
      return 'L'
  
  return grid[i][j]

def get_num_occupied_around(grid, i, j):
  occupied = 0
  around = [-1, 0, 1]

  for num in around:
    for num2 in around:
      if num == 0 and num2 == 0:
        continue

      if (0 <= i + num < len(grid)) and (0 <= j + num2 < len(grid[i + num])):
        if grid[i + num][j + num2] == '#':
          occupied += 1
          
  return occupied

def simulate_until_static():
  grid = read_input_file()
  new_grid = [[] for row in grid]

  any_change = True
  while any_change:
    any_change = False
    total_occupied = 0

    for i, row in enumerate(grid):
      for j in range(len(row)):
        next_state = get_next_state(grid, i, j)
        if next_state != grid[i][j]:
          any_change = True
        if next_state == '#':
          total_occupied += 1

        new_grid[i].append(next_state)

    grid = new_grid
    new_grid = [[] for row in grid]

  print(total_occupied)
  return total_occupied

simulate_until_static()
