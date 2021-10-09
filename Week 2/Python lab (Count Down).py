print("How many steps are we away from the cave?")
step = int(input())
print("")

for count in range(0,step,1):
    print(f"{step} steps remaining")
    step = step - 1

print("\n\nWe have reached the cave")