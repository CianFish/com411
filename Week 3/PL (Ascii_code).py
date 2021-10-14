def ASCII_code():
    print("Program Started!")
    print("Please enter a standard character:")
    sc = input()
    letter = ord(sc) #ord finds the code of the ASCII letter

    if len(sc) == 1:
        print(f"The ASCII code for {sc} is {letter}")
        print("Program ended!")
    else:
        print("Error")

print(ASCII_return())