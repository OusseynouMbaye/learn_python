# phrase = "Je suis pret"
phrase = input("[Player A ] Enter a phrase  to solve: ")

# return all index with space
# enumerate_obj = enumerate(phrase)
# print(enumerate_obj)


new_phrase = '_' * len(phrase)


# 1 : convert string en list
def convert(string):
    li = list(string)
    return li


letters_list = convert(new_phrase)

for index, letter in enumerate(phrase):
    if letter == " ":
        # 2 : replace les space par vide dans la phrase
        letters_list[index] = " "

# 3: convert list in str
letter_str = " ".join(letters_list)
print(letter_str)
