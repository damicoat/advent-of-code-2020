def get_instructions():
  with open("./input.txt") as file: 
    return [distill_line(row) for row in file]

def distill_line(line):
  action, amount = line.rstrip("\n").split(" ")
  return {
    'action': action,
    'amount': int(amount),
  }

def fix_looping(instructions = get_instructions(), acc = 0, line = 0, trying_line = None, skip_try = False):
  before_acc = acc
  seen = set()

  while line < len(instructions):
    curr = instructions[line]

    if line in seen:
      return fix_looping(instructions, before_acc, trying_line, None, True)
    else:
      action = curr['action']
      seen.add(line)

      if trying_line == None and not skip_try:
        if action == 'nop':
          action = 'jmp'
          trying_line = line
          before_acc = acc
        elif action == 'jmp':
          action = 'nop'
          trying_line = line
          before_acc = acc
      skip_try = False

      if action == 'acc':
        acc += curr['amount']
        line += 1
      elif action == 'nop':
        line += 1
      elif action == 'jmp':
        line += curr['amount']

  print(acc)
  return acc

fix_looping()