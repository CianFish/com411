def intro():
    print("Hi, I am Beep! What is your name? ")
    name = input()
    print(f"Hello {name}!")
print(intro())

def weight():
    print("\nWhat is your weight in Kilos?")
    weight = float(input())

    print("What is your height in centimeters")
    height = float(input())

    bmi = weight / height
    print(f"Your bmi is {bmi}")

    if bmi > 50:
        print("WOW! Lose some weight!")
    elif bmi < 30:
        print("Thats not healthy!")
    else:
        print("Good job!")
print(weight())

def status():
    print("\nEnter health")
    health = input()

    print("Enter shield")
    shield = input()

    print ("Enter energy:")
    energy = input()

    if "1" in health:
        print("Lives :  ♥")
    elif "2" in health:
        print("Lives :  ♥♥")
    elif "3" in health:
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
print(status())

#Another way for status would be the following:
# print("Please enter number of lives")
# lives = int(input())
# print(f"Lives:  {'♥' * lives}")