def get_instructions():
  with open("./input.txt") as file: 
    return [distill_line(row) for row in file]

def distill_line(line):
  action, amount = line.rstrip("\n").split(" ")
  return {
    'action': action,
    'amount': int(amount),
    'seen': False
  }
      
def get_actions_before_loop():
  instructions = get_instructions()
  acc = 0
  line = 0

  while True:
    curr = instructions[line]
    if curr['seen']:
      print(acc)
      return acc
    else:
      curr['seen'] = True
      action = curr['action']

      if action == 'acc':
        acc += curr['amount']
        line += 1
      elif action == 'nop':
        line += 1
      elif action == 'jmp':
        line += curr['amount']

get_actions_before_loop()