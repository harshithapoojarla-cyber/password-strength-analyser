import re

password = input("Enter Password: ")

score = 0

if len(password) >= 8:
    score += 1

if re.search("[A-Z]", password):
    score += 1

if re.search("[0-9]", password):
    score += 1

if re.search("[@#$%^&*!]", password):
    score += 1

if score <= 1:
    print("Weak Password")
elif score <= 3:
    print("Medium Password")
else:
    print("Strong Password")
    