print("Please enter a number?")
num = int(input())

fact = 0
sum = 1

while fact < num:
    fact = fact + 1
    sum = sum * fact


print(f"The factorial is {sum}")