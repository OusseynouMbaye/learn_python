a = b = ""
while not (a.isdigit() and b.isdigit()):
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxieme nombre : ")
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides")

somme = int(a) + int(b)
resultat = f"Le resulat de l'addition {a}  plus {b} est egal {somme}"
print(resultat)
