def read_input_file():
  # with open("./input.txt") as file: 
    [row.rstrip("\n") for row in ['F10', 'N3', 'F7','R90','F11']]
      

def get_manhattan_distance():
  facing_dir = ['N', 'E', 'S', 'W']
  facing = 1

  dirs = {
    'N': 0,
    'E': 0,
    'S': 0,
    'W': 0
  }

  for line in read_input_file():
    action = line[0]
    value = int(line[1:])

    if action in {'N', 'S', 'E', 'W'}:
      dirs[action] += value
    elif action in {'L', 'R'}:
      spin = 0
      if value == 90:
        spin = 1
      elif value == 180:
        spin = 2
      elif value == 270:
        spin = 3

      if action == 'L':
        facing = (facing - spin) % 4
      else:
        facing = (facing + spin) % 4
    elif action == 'F':
        dirs[facing_dir[facing]] += value

  return abs(dirs['N'] - dirs['S']) + abs(dirs['E'] - dirs['W'])

get_manhattan_distance()