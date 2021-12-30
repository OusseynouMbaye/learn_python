# nested data with list
letters = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
]
# 1 : change a value : we change e for p
# letters[1][1] = "p"  c
# print(letters[1][1])  # e
# 2 : add a new letter in dict : use .append()
letters[1].append("z")
# print(letters)
# 3 : add a new list in the list
letters.append(["k", "t", "w"])
# print(letters)
# for letter in letters:
#     print(letter)

# 2 nested data with dict
users = {
    "user-one": {"id": 1, "name": "Ouzi"},
    "user-two": {"id": 2, "name": "Sofia"},
    "user-three": {"id": 3, "name": "Amina"},
}
# add a new user in th dict
users["user-four"] = {"id": 4, "name": "Ali"}

# print(users["user-four"])
# modify user or add user
users["user-one"]["name"] = "Aida"
# print(users)

users2 = [
    {"id": 1, "name": "Oussou"},
    {"id": 2, "name": "Zach"},
    {"id": 3, "name": "Max"}
]

# add a new user
users2.append({"id": 4, "name": "dakar"})
print(users2)
