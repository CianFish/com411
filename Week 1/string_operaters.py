print("Please enter the number of lives: ")
live = input()

print("Please enter the energy level: ")
energy = input()

print("Please enter the shield level: ")
shield = input()

if "1" in live:
    print("Lives :  ♥")
elif "2" in live:
    print("Lives :  ♥♥")
elif "3" in live:
    print("Lives :  ♥♥♥")
else:
    print("Full health ")

if "1" in energy:
    print("Energy:  ♦")
elif "2" in energy:
    print("Energy:  ♦♦")
elif "3" in energy:
    print("Energy:  ♦♦♦")
else:
    print("Full energy ")

if "1" in shield:
    print("shield:  ♦")
elif "2" in shield:
    print("shield:  ♦♦")
elif "3" in shield:
    print("shield:  ♦♦♦")
else:
    print("Full shield ")