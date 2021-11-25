def replace_character_in_list(string, letters_list, entered_character):
    for index, letter in enumerate(string):
        if letter.casefold() == entered_character:
            # 2 : replace les space par vide dans la phrase
            letters_list[index] = letter

    return letters_list


# ========= Game setup =============

lives = 3

example_string = input("[Player A ] Enter a phrase  to solve: ")

new_phrase = '_' * len(example_string)


# 1 : convert string en list
def convert(string):
    li = list(string)
    return li


letters_list = convert(new_phrase)
letters_list = replace_character_in_list(example_string, letters_list, ' ')
print(f'[Player B] You must solve this phrase: {"".join(letters_list)}')

# ========= Game play =============
while lives > 0:
    entered_character = input("[Player B ] Please guess a letter: ")
    if entered_character in example_string.casefold():
        letters_list = replace_character_in_list(example_string,
                                                 letters_list,
                                                 entered_character)

        print(" ".join(letters_list))

    else:
        lives -= 1
        print(f'{entered_character} not found in {" ".join(letters_list)} '
              f'{lives} LIVES REMAINING')

    # ========= Game end =============
    if "_" not in " ".join(letters_list):
        print("YOU WIN !!!")
        break

    if lives < 1:
        print("GAME OVER!!!")
        print('The answer was' + example_string)
