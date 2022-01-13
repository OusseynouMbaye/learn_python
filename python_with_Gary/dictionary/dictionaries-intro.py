user = {"firt_name": "Ouzinem",
        "address": "St-Georges",
        "favorite_sport": {1: "swim", 2: "cycling"},
        "person": {1: "moi", 2: "toi"}}

# print(user["favorite_sport"].values())
# print(user["favorite_sport"])
# print(user.values())
# print(user.keys())
# user["taille"] = 180
# user["favorite_sport"] = "Basket"
# print(user.fromkeys())
# Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
# print(marks)

# for item in marks.items():
#     print(item)

# Output: ['English', 'Math', 'Science']
# print(list(sorted(marks.keys())))

# employes = {
#             "01": {
#                 "identite": {
#                     "prenom": "Pierre",
#                     "nom": "Dupont"
#                     }
#                 }
#             }

# resultat = employes.get('03',{}).get("identite",{}).get("prenom",{})
# print(resultat)

employes = {
    "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
    "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
    "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
}

age_paul = employes.get("id01", {}).get("age", {})
employes["id02"]['age'] = 26
del employes['id03']  # employes.pop("id03")
print(employes)
