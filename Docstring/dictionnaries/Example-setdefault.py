names = {
            "Patrick": "Smith",
            "Julie": "Mercier",
            "Maxime": "Moulin",
            "Gérard": "Moulin",
            "Rose": "Mercier",
            "Clara": "Smith",
            "John": "Moulin",
            "Michel": "Smith",
        }
resultat = {}
for key, value in names.items():
    resultat.setdefault(value, []).append(key)

