print("What was the first product you bought in Tesco today?")
product1 = input()

print("What was the first product you bought in Tesco today?")
product2 = input

if (product1 == "veg") and (product2 == "beef"):
    print("What are you going to make?")
    make = input()
    if (make == "Chilli") or (make == "Stew"):
        print("Very nice!")
    else:
        print("What is wrong with you!")
elif (product1 == "veg") and (product2 == "chocolate"):
    print("You only bought one thing on the list")
else:
    print("You didnt buy anything on the list")
