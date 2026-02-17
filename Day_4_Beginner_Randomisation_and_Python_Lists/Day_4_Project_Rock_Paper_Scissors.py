import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) '''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

scissors = '''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
print("Welcome to rock paper and scissors game.s")


choices = [rock, paper, scissors]
userChoice = int(input("Enter 0 for rock, 1 for paper, 2 for scissors: "))
computerChoice = random.randint(0, 2)

if userChoice < 0 or userChoice > 2:
    print("Invalid choice!")
else:
    print("You chose:")
    print(choices[userChoice])

    print("Computer chose:")
    print(choices[computerChoice])

    if userChoice == computerChoice:
        print("It's a tie!")
    elif (userChoice == 0 and computerChoice == 2) or (userChoice == 1 and computerChoice == 0) or (userChoice == 2 and computerChoice == 1):
        print("You win!")
    else:
        print("You lose!")
