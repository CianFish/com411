def ASCII_char():
    print("Program Started!")
    print("Please enter an ASCII code:")
    code = int(input())
    character = chr(code)

    if code >=32 and code <=126:
        print(f"The character represented by the ASCII code {code} is: {character}")
        print("Program Ended!")
    else:
        print("Error")

print(ASCII_char())