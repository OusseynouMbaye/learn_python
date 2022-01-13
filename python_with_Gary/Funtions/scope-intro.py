# number = 200
#
#
# def myfunc():
#     print(number)
#
#
# myfunc()

employes = {
    "01": {
        "identite": {
            "prenom": "Pierre",
            "nom": "Dupont"
        }
    }
}

resultat = employes.get('03', {}).get("identite", {}).get("prenom", {})
print(resultat)
