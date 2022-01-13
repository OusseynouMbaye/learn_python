chemin = r"C:\Users\Ouzinem\Desktop\onlineCourse\learn_python\python_with_Gary\Files\programming-languages.txt"
# chemin = "/c/Users/Ouzinem/Documents/cvouzin"
# print(chemin)

# file = open(chemin, 'r')
# print(file.read())
# file.close()

# method 2 : on a pas besoin de faire un .close()
with open(chemin, 'a') as file_name:
    file_name.write("\nNodeJs")
    print(file_name.read().splitlines())
    # print(contenu)
# contenu = repr(file_name.read())
# splitlines() va enlver les \n et tout mettre dans une list
