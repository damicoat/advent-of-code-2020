import heapq 

def read_input_file():
  # with open("./input.txt") as file: 
  for row in [16,10,15,5,1,11,7,19,6,12,4]:
    yield row
      # yield int(row.rstrip("\n"))

def get_sorted_array():
  h = []
  for num in read_input_file():
    heapq.heappush(h, num)

  return [heapq.heappop(h) for i in range(len(h))]

def num_arrangements(sorted = None, i = 0, count = 0, start = 0, skipped_nums = set()):
  h = sorted or get_sorted_array()

  

num_arrangements()