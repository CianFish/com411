import random as rnd
from random import gauss

print("Please enter the minimum value:")
min = int(input())

print("\nPlease enter the maximum value: ")
max = int(input())

print(f"\nI am thinking of a number between {min} and {max}. Can you guess what it is?")
ans = int(input())
computer_ans = gauss(min, max)




#for _ in range (0, max, 1):
#    if ans == computer_ans:
#        print("Congratulations! You guessed my number!")
#    elif ans >= computer_ans:
#        print("Your guess is to high.")
#        print("\nTry again")
#    elif ans <= computer_ans:
#        print("Your guess is too low")
#        print("\nTry again")