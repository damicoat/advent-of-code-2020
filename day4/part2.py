import re

def read_input_file():
  with open("4_input.txt") as file: 
    for row in file:
      yield row

def is_valid_byr(val):
  val = int(val)
  return 1920 <= val and val <= 2002

def is_valid_iyr(val):
  val = int(val)
  return 2010 <= val and val <= 2020

def is_valid_eyr(val):
  val = int(val)
  return 2020 <= val and val <= 2030

def is_valid_hgt(val):
  if len(val.split("cm")) == 2:
    num = int(val.split("cm")[0])
    return 150 <= num and num <= 193
  else:
    num = int(val.split("in")[0])
    return 59 <= num and num <= 76

def is_valid_hcl(val):
  pattern = re.compile('^#[a-f0-9]{6}$')
  return bool(pattern.match(val))

def is_valid_ecl(val):
  accepted_vals = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth',}
  return val in accepted_vals

def is_valid_pid(val):
  pattern = re.compile('^[0-9]{9}$')
  return bool(pattern.match(val))

def is_valid_passport(record):
  required_fields = [
    ['byr', is_valid_byr],
    ['iyr', is_valid_iyr],
    ['eyr', is_valid_eyr],
    ['hgt', is_valid_hgt],
    ['hcl', is_valid_hcl],
    ['ecl', is_valid_ecl],
    ['pid', is_valid_pid],
    # 'cid',
  ]

  for field_rules in required_fields:
    field, is_valid = field_rules[0], field_rules[1]
    if field not in record or not is_valid(record[field]):
      return False

  return True

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

num_valid_passports()