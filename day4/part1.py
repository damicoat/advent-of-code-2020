def read_input_file():
  with open("./input.txt") as file: 
    for row in file:
      yield row

def num_valid_passports():
  num_passports = 0
  record = {}

  for line in read_input_file():
    if line == "\n":
      # newline is record delimiter
      is_valid = is_valid_passport(record)
      if is_valid:
        num_passports += 1
      
      record = {}
    else:
      # build up records from rows
      fields = line.rstrip("\n").split(" ")
      for field in fields:
        k_v = field.split(":")
        record[k_v[0]] = k_v[1]
  
  # no newline at EOF means checking final record
  if is_valid_passport(record):
    num_passports += 1

  print(num_passports)
  return num_passports

def is_valid_passport(record):
  required_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid',
  ]

  for field in required_fields:
    if field not in record:
      return False

  return True

num_valid_passports()