import heapq 

def read_input_file():
  with open("./input.txt") as file: 
    for row in file:
      yield int(row.rstrip("\n"))

def construct_heap():
  h = []
  for num in read_input_file():
    heapq.heappush(h, num)
  return h

def joltage_diff():
  diffs = {1: 0, 3: 0}

  h = construct_heap()
  start = 0
  while len(h) > 0:
    el = heapq.heappop(h)
    diffs[el - start] += 1
    start = el
  
  print(diffs[1] * (diffs[3] + 1))
  return diffs[1] * (diffs[3] + 1)

joltage_diff()