# Heads or Tails
# import random

# number = random.randint(0, 10)

# if number % 2 == 0:
#     print("Head")
# else:
#     print("Tails")

# who will pay the bill?

# friends = ["mert", "selin", "hakan", "umut", "salih"]

# random_index = random.randint(0, 5)
# print(friends[random_index])
# print(len(friends))


# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)
# print(dirty_dozen[0])
# print(dirty_dozen[1])
# print(dirty_dozen[1][1])
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])

# ------------------------------------------------------------------------------------

# Rock, paper, scissors game project

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

ascii_art = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}


list_choice = ["rock", "paper", "scissors"]


player_choice = input("which one is do you want choose?"
                       "'rock', 'paper', or 'scissors': ")
print("user choice: ", ascii_art[player_choice]) 

computer_choice = random.choice(list_choice)
print("computer choice: ", ascii_art[computer_choice]) 


if player_choice == "rock" and computer_choice == "scissors":
    print("you choosed: {} and computer choosed:{} ".format(player_choice, computer_choice))
    print("you won")
elif player_choice == "rock" and computer_choice == "paper":
    print("you choosed: {} and computer choosed:{} ".format(player_choice, computer_choice))
    print("you lost")
elif player_choice == "rock" and computer_choice == "rock":
    print("you choosed: {} and computer choosed:{} ".format(player_choice, computer_choice))
    print("no win no lost")
elif player_choice == "paper" and computer_choice == "paper":
    print("you choosed: {} and computer choosed:{} ".format(player_choice, computer_choice))
    print("no win no lost")
elif player_choice == "paper" and computer_choice == "rock":
    print("you choosed: {} and computer choosed:{} ".format(player_choice, computer_choice))
    print("you won")
elif player_choice == "paper" and computer_choice == "scissors":
    print("you choosed: {} and computer choosed:{} ".format(player_choice, computer_choice))
    print("you lost")
elif player_choice == "scissors" and computer_choice == "scissors":
    print("you choosed: {} and computer choosed:{} ".format(player_choice, computer_choice))
    print("no win no lost")
elif player_choice == "scissors" and computer_choice == "rock":
    print("you choosed: {} and computer choosed:{} ".format(player_choice, computer_choice))
    print("you lost")
elif player_choice == "scissors" and computer_choice == "paper":
    print("you choosed: {} and computer choosed:{} ".format(player_choice, computer_choice))
    print("you won")


