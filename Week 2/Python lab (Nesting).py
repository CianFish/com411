#Ask about this one
print("Please enter a sequence")
seq = input()

print("Please enter the character for the marker")
char = input()

marker1 = -1
marker2 = -1

for count in range(0, len(seq), 1):
    letter = seq[count]

    if letter == char:
        if (marker1 == -1):
            marker1 = count
    else:
        marker2 = count

print(f"The distance between the marker is {marker2 - marker1 - 1}")







