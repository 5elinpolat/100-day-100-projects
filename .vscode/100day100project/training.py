# Password Generator Project

import random

letters = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','r','s']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%', '(', ')', '*', '+']

print("Welcome to the passwords generator!")

total_length = 8

nr_letters = total_length - 2

remaining_length = total_length - nr_letters

nr_symbols = remaining_length - 1

nr_numbers = remaining_length - nr_symbols

password_list = []

for i in range(0, nr_letters):
    password_list.append(random.choice(letters))

for i in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for i in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""

for i in password_list:
    password += i

print(f"your password is: ",password)