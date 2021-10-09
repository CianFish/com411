cal = 0
cal1 = 0

print("How many numbers should I sum up?")
num = int(input())

while cal < num:
    print("Please enter number ", end="")
    cal = cal + 1
    print(f"{cal} of {num}")
    ans = int(input())
    cal1 = ans + cal1


print(f"The answer is {cal1}")