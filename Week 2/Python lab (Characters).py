print("What strange markings do you see?")
see = input()

for position in range(0,len(see),1):
    print(f"index {position}: {see[position]}")

print("\nDone!")