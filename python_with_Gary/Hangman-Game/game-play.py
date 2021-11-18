def replace_character_in_list(string, letters_list, entered_character):
    for index, letter in enumerate(string):
        if letter.casefold() == entered_character:
            # 2 : replace les space par vide dans la phrase
            letters_list[index] = letter

    return letters_list


lives = 1
letter_str = ""
example_letter = "String"
new_phrase = '_' * len(example_letter)


# 1 : convert string en list
def convert(string):
    li = list(string)
    return li


letters_list = convert(new_phrase)

while lives > 0:
    entered_character = 'z'
    if entered_character in example_letter.casefold():
        letters_list = replace_character_in_list(example_letter,
                                                 letters_list,
                                                 entered_character)

        print(" ".join(letters_list))

    else:
        lives -= 1
        print(f'{entered_character} not found in {" ".join(letters_list)} '
              f'{lives} LIVES REMAINING')

    print(lives)

    break
