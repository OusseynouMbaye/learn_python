user = {"firt_name": "Ouzinem",
        "address": "St-Georges", 
        "favorite_sport": {1:"swim",2: "cycling"},
         "person": {1: "moi", 2: "toi"}}

print(user["favorite_sport"].values())
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
