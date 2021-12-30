import json
import os
import sys

CURRENT_DIR = os.path.dirname(__file__)  # recuperation du dossier parent :nom du dossier
LISTE_PATH = os.path.join(CURRENT_DIR, "liste.json")
# MY_LIST = []

MENU = """Choisissez parmis les 5 options  suivantes : 
1: Ajouter un element 'a la liste
2: Retirer un element a la liste
3: Afficher la liste
4: Vider la liste
5 : Quitter
 votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

# 1: verifie si la liste existe
if os.path.exists(LISTE_PATH):
    # si la liste existe on recupere le contenu
    with open(LISTE_PATH, "r") as filename:
        MY_LIST = json.load(filename)
else:
    MY_LIST = []

while True:
    user_choice = ""
    # on verifie si user a rentrer un nombre valide
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")

    if user_choice == "1":
        item = input("Entrer le nom d'un element a ajouter a la "
                     "liste de course: ")
        MY_LIST.append(item)
        print(f"L'element {item} a bien ete ajoute a la liste.")

    elif user_choice == "2":  # Retirer un element
        item = input("Entrer le nom d'un element a retirer de la "
                     "liste de courses: ")
        if item in MY_LIST:
            MY_LIST.remove(item)
            print(f"L'element {item} a bien ete retire a la liste.")
        else:
            print(f"L'element {item} n'est pas dans la liste.")
    elif user_choice == "3":  # Afficher la liste
        if MY_LIST:
            print("Voici le contenu de votre liste : ")
            for i, item in enumerate(MY_LIST, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun element")
    elif user_choice == "4":
        MY_LIST.clear()
        print("La liste a ete videe de son contenu.")
    elif user_choice == "5":
        # ecrit la liste sur le disque
        with open(LISTE_PATH, "w") as filename:
            json.dump(MY_LIST, filename, indent=4)
        print("A bientot !")
        sys.exit()

    print("_" * 50)
