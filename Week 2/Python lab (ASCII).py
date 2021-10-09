print("How many bars should be charged?")
bar = int(input())

bars_charged = 0

while bars_charged < bar:
    print(f"Charging:", end="")
    bars_charged = bars_charged + 1
    sum1 = bars_charged * "█ "
    print(f"{(sum1)}")

print("\nThe battery is fully charged")