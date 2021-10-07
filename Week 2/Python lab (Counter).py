print("Please enter the first whole number.")
fn = int(input())
print("Please enter the second whole number.")
sn = int(input())
print("Please enter the third whole number.")
tn = int(input())

if (fn%2) == 0 and (sn%2) == 0 and (tn%2) == 0:
    print("There was 3 even numbers.")
elif (fn%2) != 0 and (sn%2) == 0 and (sn%2) == 0:
    print("There was 1 odd and 2 even numbers")
elif (fn % 2) == 0 and (sn % 2) != 0 and (sn % 2) == 0:
    print("There was 1 odd and 2 even numbers")
elif (fn%2) == 0 and (sn%2) == 0 and (sn%2) != 0:
    print("There was 1 odd and 2 even numbers")
elif (fn%2) != 0 and (sn%2) != 0 and (sn%2) == 0:
    print("There was 2 odd and 1 even numbers")
elif (fn%2) != 0 and (sn%2) == 0 and (sn%2) != 0:
    print("There was 2 odd and 1 even numbers")
elif (fn%2) == 0 and (sn%2) != 0 and (sn%2) != 0:
    print("There was 2 odd and 1 even numbers")
else:
    print("There was 3 odd numbers")