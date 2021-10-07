print("What type of adventure should I have?")
adv = input()

if (adv == "scary") or (adv == "short"):
    print("Entering the dark forest")
elif (adv == "safe") or (adv == "long"):
    print("Taking the safe route")
else:
    print("Not sure which route to take.")