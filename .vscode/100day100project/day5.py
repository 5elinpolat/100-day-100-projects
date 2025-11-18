# find max scor
# student_scores = [100, 500, 200, 300, 400]

# max_score = 0

# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(max_score)

# ---------------------------------

# total = 0

# for i in range(1,101):
#     total += i
# print(total)
# -----------------------------
# for i in range(1,101):
#     if i % 5 == 0 and i % 3 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# ---------------------------------
# Password Generator Project

import random

letters = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','r','s']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%', '(', ')', '*', '+']

print("Welcome to the passwords generator!")
nr_letters = int(input("how many letters would you like in your message? \n"))
nr_symbols = int(input("how many symbols would you like? \n"))
nr_numbers = int(input("how many numbers would you like \n"))


#randomly choice from list with python library
password_list = []

for i in range(0, nr_letters ):
    password_list.append(random.choice(letters))

for i in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

for i in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ''

for i in password_list:
    password += i
  
print(f"your password is:", password)