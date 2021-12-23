import sys

choice = ""
MY_LIST = []

MENU = """Choisissez parmis les 5 options  suivantes : 
1: Ajouter un element 'a la liste
2: Retirer un element a la liste
3: Afficher la liste
4: Vider la liste
5 : Quitter
 votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

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
        item = input("Entrer le nom d'un element a retir de la "
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
        print("A bientot !")
        sys.exit()

    print("_" * 50)
