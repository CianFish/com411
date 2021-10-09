print("What phrase do you see?")
phrase = input()

print("\nReversing...\n")
print("The phrase is ", end="")

for reverse in range(len(phrase)-1,-1,-1):
    print(f"{phrase[reverse]}", end="")

