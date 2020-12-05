def read_input_file():
  with open("./input.txt") as file: 
    for row in file:
      yield row.split(" ")

def is_valid_pass(pass_row):
  num_times, letter, password = pass_row

  letter = letter[0]
  min_times, max_times = [int(x) for x in num_times.split("-")]
  occurrences = len(password.split(letter)) - 1

  return min_times <= occurrences and occurrences <= max_times

def get_num_valid_pass():
  num_valid_pass = 0

  lines = read_input_file()
  for line in lines:
    if (is_valid_pass(line)):
      num_valid_pass += 1
  
  print(num_valid_pass)
  return num_valid_pass

get_num_valid_pass()