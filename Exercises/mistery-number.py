import sys
from random import random, randint

# for i in range(10):
MENU = "*** Le jeu du nombre mystere *** "
number_to_find = randint(1, 10)
remaining_attempts = 5
print(MENU)
while remaining_attempts > 0:
    print(f"il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")

    user_choice = input("Devinez le nombre : ")
    if not user_choice.isdigit():
        print("Veuillez entrer un nombre valide ")
        continue

    user_choice = int(user_choice)

    if number_to_find > user_choice:
        print(f"the mystery numb is bigger than {user_choice}")
    elif number_to_find < user_choice:
        print(f"the mystery numb is smaller {user_choice}")
    else:
        break
        # print(f"the mystery numb is equal {number_to_find}")
    remaining_attempts -= 1

if remaining_attempts == 0:
    print(f"Dommage ! le nombre mystere etait {number_to_find}")
else:
    print(f"Bravo ! Le nombre mystere etait bien {number_to_find} !")
    print(f"Tu as trouve le nombre en {6 - remaining_attempts} essai ")

print("Fin du jeu.")
