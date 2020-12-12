def read_input_file():
  with open("./input.txt") as file: 
    for row in file:
      yield row.rstrip("\n")

def get_manhattan_distance():
  facing_dir = ['N', 'E', 'S', 'W']

  waypoint = {
    'N': {
      'value': 1,
      'pos': 0,
    },
    'E': {
      'value': 10,
      'pos': 1,
    },
    'S': {
      'value': 0,
      'pos': 2,
    },
    'W': {
      'value': 0,
      'pos': 3,
    },
  }

  dirs = {
    'N': 0,
    'E': 0,
    'S': 0,
    'W': 0,
  }

  for line in read_input_file():
    action = line[0]
    value = int(line[1:])

    if action in {'N', 'S', 'E', 'W'}:
      waypoint[action]['value'] += value
    elif action == 'F':
      for key in waypoint:
        dirs[key] += waypoint[key]['value'] * value
    elif action in {'L', 'R'}:
      spin = 0
      if value == 90:
        spin = 1
      elif value == 180:
        spin = 2
      elif value == 270:
        spin = 3

      new_waypoint = {}
      for key in waypoint:
        if action == 'L':
          new_facing_pos = (waypoint[key]['pos'] - spin) % 4
        else:
          new_facing_pos = (waypoint[key]['pos'] + spin) % 4

        new_direction = facing_dir[new_facing_pos]
        new_waypoint[new_direction] = {
          'value': waypoint[key]['value'],
          'pos': waypoint[new_direction]['pos'],
        }

      waypoint = new_waypoint

  print(abs(dirs['N'] - dirs['S']) + abs(dirs['E'] - dirs['W']))
  return abs(dirs['N'] - dirs['S']) + abs(dirs['E'] - dirs['W'])

get_manhattan_distance()