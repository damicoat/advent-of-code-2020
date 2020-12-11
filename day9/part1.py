def read_input_file():
  with open("./input.txt") as file: 
    for row in file:
      yield int(row.rstrip("\n"))

# first number that is not the sum of 2
# of the previous 25 numbers

def find_two_entries(prev5, target):
  needed = {}
  for num in prev5:
    num_needed = target - num
    needed[num_needed] = True

    if num in needed:
      return True

  return False

def find_culprit():
  arr = []
  for num in read_input_file():
    if len(arr) < 25:
      arr.append(num)
    elif len(arr) == 25:
      res = find_two_entries(arr, num)
      if not res:
        print(num)
        return num
      else:
        arr.pop(0)
        arr.append(num)

find_culprit()