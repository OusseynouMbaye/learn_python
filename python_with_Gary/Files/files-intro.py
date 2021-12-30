# languages_file = open('programming-languages.txt', 'a')

# Read : read all file
# print(languages_file.read())

# readline line by line
# print(languages_file.readline())

# readline :return list of all element to the file
# file_list = languages_file.readlines()  # print(file_list[2])

# for line in file_list:
#     print(line)

# write  : for write we can use w or a
#  w : ecrase all data or a append new text
# languages_file = open('programming-languages.txt', 'a')
# languages_file.write("\nJava")
# languages_file.close()

# context
with open('programming-languages.txt', 'a') as languages_file:
    languages_file.write("\nC#")
    print("processing...")

print("no longer dealing with the file.")
