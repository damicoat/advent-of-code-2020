import queue

def read_input_file():
  with open("./input.txt") as file: 
    for row in file:
      yield row.rstrip("\n")

def construct_rules():
  rules = {}
  for line in read_input_file():
    bag_contains_key, contained_bags = line.split(" bags contain ")

    if contained_bags != "no other bags.":
      contained_bags = contained_bags.split(", ")

      for color_rules in contained_bags:
        # split on first occurence of space!
        num, color = color_rules.split(" bag")[0].split(" ", 1)
        num = int(num)
        
        if bag_contains_key in rules:
          rules[bag_contains_key].append([color, num])
        else:
          rules[bag_contains_key] = [[color, num]]

  return rules

def shiny_gold_contains():
  total = 0
  rules = construct_rules()

  q = rules["shiny gold"]
  while len(q) > 0:
    [color, num] = q.pop()
    total += num

    if color in rules:
      for [inner_color, inner_num] in rules[color]:
        q.append([inner_color, inner_num * num])
    
  print(total)
  return total

shiny_gold_contains()
