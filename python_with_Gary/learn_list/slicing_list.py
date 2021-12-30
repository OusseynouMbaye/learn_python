numbers = [1, 2, 3, 4, 5]
# print(numbers[-5:-3])

name = "Ousseynou Mbaye"
# print(name[-5::2])

birds = "birds.jpg"
men = "men.png"


def removeFileType(filename):
    return filename[:-4]


# print(removeFileType(birds))
input_file = input("enter un file:")
print(removeFileType(input_file))
