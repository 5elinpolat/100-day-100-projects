# Pizza Deliveries

# print("welcome to python pizza deliveries")
# size = input("what size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")


# # todo: work out how much they need to pay based on their pepperoni choice

# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else :
#     bill += 25


# # todo: work out how much to add to their bill based on the their pepperoni choice
    
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     elif size == "M" or "L" :
#         bill += 3

# # todo: work out their final amount based on if they want extra cheese
        
# if extra_cheese == "Y":
#     bill += 1



# print (f"Your Payment is: £", {bill} )


#  Final Project : Treasure ISLAND

print('''
         888                                                          
         888                                                          
         888                                                          
         888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
         888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
         888   888    88888888.d888888"Y8888b.888  888888    88888888 
         Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
         "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888"  ''')

print( " welcome to Treasure Island")
print("Your mission is find the treasure.")
print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')
      

print("You're the cross road. Where do want to go? Right or Left?")

choice = input("right or left?: ")

if choice == "right":
    print("You fell into a hole. Game Over")
else:
    print("You've come to lake.There i s island middle of the lake.Do you want to wait for a boat or swim")


choice = input("choice wait or swim: ")

if choice == "swim" :
    print("Attacked by trout. game Over")
else:
    print("You've reached a Door.you need choice a one door")


choice = input("which color of door do you want chooice? red,blue or yellow? ")

if choice == "red":
    print("burned by fire, GAME OVER.")
elif choice == "blue":
    print("eaten by beast. game over")
else:
    print("You win")