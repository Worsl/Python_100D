import random
import time

print("Welcome to the rock scissors paper")

name = input("Challenger, please enter your name: ")

choice = int(input("input 0 for ROCK , 1 for SCISSORS and 2 for PAPER: "))
print(f"{name} chose {choice}!")
time.sleep(2.5)

if (choice == 0):
    print("You used ROCK!")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif (choice == 1):
    print("You used SCISSORS! ")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

elif (choice == 2):
    print("You used PAPER! ")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

else:
    print("Number entered is out of bounds")


machine = random.randint(0,2)
print("\n \n \n \n \n")
print("Waiting for the computer...")

time.sleep(2)
if (machine == 0):
    print("machine used ROCK!")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif (machine == 1):
    print("machine used SCISSORS! ")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

elif (machine == 2):
    print("machine used PAPER! ")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

time.sleep(2.5)
#the case for user using ROCK(choice 0)
if choice == 0:
    if (choice - machine == 0):
        print("DRAW!")
    elif (choice - machine == -1):
        print("WINNER")
    elif (choice - machine == -2):
        print("Sb u lose HAHA")

if choice == 1:
    if  (choice - machine == 0):
        print("DRAW!" )
    elif (choice - machine == 1 ):
        print("sb u lose HAHA!")
    elif (choice - machine == -1):
        print("WINNER! ")

if choice == 2:
    if (choice - machine == 0):
        print("Draw")
    elif (choice - machine == 2):
        print("WINNER!")
    elif(choice - machine == 1):
        print("Loser")

print("End of program")
time.sleep(10)
