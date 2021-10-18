def sum_weight(Beep, Bop):
    sum = Beep + Bop
    return sum

def calc_avg_weight(Beep, Bop):
    avg = (Beep + Bop) / 2
    return avg

def run():
    print("What is the weight of Beep?")
    Beep = int(input())
    print("\nWhat is the weight of Bop?")
    Bop = int(input())
    print("What would you like to calculate (sum or average)?")
    sora = input()

    if sora == "sum":
        print(sum_weight(Beep, Bop))
        print(f"The sum of Beep and Bop's weight is {sum_weight(Beep,Bop)}")
    else:
        print(calc_avg_weight(Beep, Bop))
        print(f"The average of Beep and Bop's weight is {calc_avg_weight(Beep,Bop)}")

run()