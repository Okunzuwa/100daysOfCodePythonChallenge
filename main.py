import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")

image = [rock, paper, scissors]
users_choice = int(choice)


if users_choice >= 3 or users_choice < 0:
  print("You have typed an invalid code. You lose!")
else:
  print(image[users_choice])
  
  computers_choice = random.randint(0, 2)
  print(f"Computer chose:\n{image[computers_choice]}")
  
  if users_choice == 2 and computers_choice == 0:
    print("You lose!")
  elif users_choice == 0 and computers_choice == 2:
    print("You win!")
  elif users_choice > computers_choice:
    print("You win!")
  elif users_choice == computers_choice:
    print("It's a draw")
  else:
    print("You lose!")