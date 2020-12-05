def read_input_file():
  with open("./input.txt") as file: 
    for row in file:
      yield row.split(" ")

def is_valid_pass(pass_row):
  num_times, letter, password = pass_row
  
  letter = letter[0]
  # no concept of 0 index in input
  pos_1, pos_2 = [(int(x) - 1) for x in num_times.split("-")]
  is_pos_1_letter = len(password) > pos_1 and password[pos_1] == letter
  is_pos_2_letter = len(password) > pos_2 and password[pos_2] == letter

  # XOR (a and not b) or (b and not a)
  return is_pos_1_letter != is_pos_2_letter

def get_num_valid_pass():
  num_valid_pass = 0

  lines = read_input_file()
  for line in lines:
    if (is_valid_pass(line)):
      num_valid_pass += 1
  
  print(num_valid_pass)
  return num_valid_pass

get_num_valid_pass()
