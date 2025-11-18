# print("Hello"[0])
# print("Hello"[-2])

# print(123 + 234)
# print(124_343)


############### # Data type ############
# print(type("hello"))
# print(type(123))

# # Convert the data #
# print(int("abc"))

# print("Number of letter in your name:" + len(input("Enter your name:")))# give an error cause different type

# print("Number of letter in your name:" + str(len(input("Enter your name:"))))


####### mathematical opertions###############

# print(2**2)

# bmi = 84 / 1.65 ** 2

# print(int(bmi))
# print(round(bmi))
# print(round(bmi,2))

# score = 0
# height = 1.8
# is_winning = True

# print(f"Your score is = {score}, your height is {height}, you are winning is :{is_winning}")

########   TIP CALCULATOR PROJECT  ########  

print("Welcome to the TIP CALCULATOR")

bill = float((input("What was the total bill?: ")))

tip = int(input("What percentage tip would you like to give? Please just enter number: " ))

people = int(input("How many people to split the bill: "))
 
tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: $ {final_amount}")

