import json

# method to append with dict
# with open("data.json", 'r') as file_name:
#     data = json.load(file_name)
#
# data["4"] = "KeurGui"
#
# with open("data.json", 'w') as file_name:
#     json.dump(data, file_name, indent=4)

# methode to append with List
# 1 lire fichier
with open("list.json", 'r') as file_name:
    my_list = json.load(file_name)

# 2 : ecriture
my_list.append(4)

with open("list.json", 'w') as file_name:
    json.dump(my_list, file_name, indent=4)
