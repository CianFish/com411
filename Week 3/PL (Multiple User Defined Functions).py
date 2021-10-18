def display_ladder(steps):
  print("| |")
  print("***")
  print("| |")
  for s in range(0, steps - 1, 1):
    print("***")
    print("| |")

def create_ladder():
  print("How many steps remain?")
  steps = int(input())
  display_ladder(steps)

create_ladder()