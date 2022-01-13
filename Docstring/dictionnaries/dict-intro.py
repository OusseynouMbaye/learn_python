my_dict = {
    1: {"prenom": "Jules",
        "age": 22,
        "employe": "Roi",
        "Sport": {1: "Tennis", 2: "Basket"}},
    2: {"prenom": "Cesar",
        "age": 22,
        "employe": "Empereur",
        "Sport": {1: "Tennis", 2: "Basket"}},
    3: {"prenom": "Cleopatre",
        "age": 22,
        "employe": "Reine",
        "Sport": {1: "Tennis", 2: "Basket"}}
}
# pour modfier une valeur
my_dict[1]["prenom"] = "Julie"
my_dict[1]["Sport"][2] = "Soccer"

# creer un nouvel item
my_dict[1]["taille"] = 150

# del :  Pour supprimer
if "age" in my_dict[2]:
    del my_dict[2]["age"]


# boucle sur un dictionary
for keys, value in my_dict.items():
    print(keys, value)
