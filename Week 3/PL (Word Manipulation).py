def display_in_box(special, ans):
    print("-" + (len(special) * "-") + "-")
    print("|" + special + "|")
    print("-" + (len(special) * "-") + "-")

def lower_case(special):
    final_lower =  special.lower()
    print("\n" + final_lower)

def upper_case(special):
    final_upper = special.upper()
    print("\n" + final_upper)

def display_mirrored(special):
    sl = len(special)
    sliceds = special[sl::-1]
    print("\n" + special + " | " + sliceds)

def repeat(special):
    print("\nHow many times would you like to repeat the special word?")
    n_of_t = int(input())
    final_upper = special.upper()
    final_lower = special.lower()

    for x in range(0, n_of_t, 1):
        print(final_lower)
        print(final_upper)



def manipulate_cyrptic():
    print("Please enter the special word")
    special = input()
    print("\nPlease choose one of the following:")
    print("1" + ") Display in a box")
    print("2" + ") Display lower-case")
    print("3" + ") Display Upper-case")
    print("4" + ") Display Mirrored")
    print("5" + ") Repeat")
    ans = input()

    if ans == "1":
        display_in_box(special, ans)
    elif ans == "2":
        lower_case(special)
    elif ans == "3":
        upper_case(special)
    elif ans == "4":
        display_mirrored(special)
    elif ans == "5":
        repeat(special)





manipulate_cyrptic()