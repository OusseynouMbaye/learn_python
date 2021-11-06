phrase = "Je suis pret"

# index = phrase.index(" ")  # find(" ") index(" ") return first index with space
# print(index)
enumerate_obj = enumerate(phrase)
# print(enumerate_obj)


new_phrase = '_' * len(phrase)

for index, letter in enumerate(phrase):
    if letter == " ":
        new_phrase[index] = " "

print(new_phrase)
