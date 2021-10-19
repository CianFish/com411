import random
import random as rnd

def asking_user(min, max,):
    print("Please enter the minimum value:")
    min = int(input())

    print("\nPlease enter the maximum value: ")
    max = int(input())

    repeating_question(min, max)


def repeating_question(min, max):
    computer_ans = random.randrange(min, max)

    print(f"I am thinking of a number between {min} and {max}.\nCan you guess what is is?")

    correct_ans = False

    while not correct_ans:
        print("Please enter a number:")
        ans = int(input())

        if ans == computer_ans:
          print("Congratulations! You guessed my number!")
          correct_ans = True
        elif ans >= computer_ans:
            print("Your guess is to high.\nTry again:")
        elif ans <= computer_ans:
            print("Your guess is to low.\nTry again:")

    print("Game over!")


asking_user(min, max)

#for _ in range (0, max, 1):
#    if ans == computer_ans:
#        print("Congratulations! You guessed my number!")
#    elif ans >= computer_ans:
#        print("Your guess is to high.")
#        print("\nTry again")
#    elif ans <= computer_ans:
#        print("Your guess is too low")
#        print("\nTry again")