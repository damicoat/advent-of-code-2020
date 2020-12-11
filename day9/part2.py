import math

def read_input_file():
  with open("./input.txt") as file: 
    return [int(row.rstrip("\n")) for row in file]

part1_answer = 776203571

def sliding_window():
  sequence = read_input_file()
  sum = 0
  start = 0
  end = 0

  while start <= end:
    if sum < part1_answer:
      sum += sequence[end]
      end += 1
    elif sum > part1_answer:
      sum -= sequence[start]
      start += 1
    else:
      mini = min(sequence[start:end + 1])
      maxi = max(sequence[start:end + 1])
      print(maxi + mini)
      return maxi + mini

sliding_window()