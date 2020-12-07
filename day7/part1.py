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
        color = color_rules.split(" bag")[0][2:]
        
        if color in rules:
          rules[color].add(bag_contains_key)
        else:
          rules[color] = set([bag_contains_key])

  return rules

def contain_shiny_gold():
  contain_shiny_gold = set()
  rules = construct_rules()
  
  q = rules["shiny gold"]
  while len(q):
    color = q.pop()
    contain_shiny_gold.add(color)
    if color in rules:
      for item in rules[color]:
        q.add(item)
  
  print(len(contain_shiny_gold))
  return len(contain_shiny_gold)

contain_shiny_gold()