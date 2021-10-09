print("How many rows should I have?")
row = int(input())

print("\nHow many column should I have?")
col = int(input())

print("\nHere I go:\n")

for count in range(0, row, 1):
    for number in range(0, col, 1):
        sum1 = number * ":-) "
        print(f"{sum1}  ", end="")
    print()

print("\n\nDone!")