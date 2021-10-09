#ask why + 1
print("What level of brightness is required?")
level = int(input())

for brightness in range(2,level + 1,2):
    print(f"Beep's brightness level: {'*' * brightness}")
    print(f"Bop's brightness level: {'*' * brightness}")
    print("\n")