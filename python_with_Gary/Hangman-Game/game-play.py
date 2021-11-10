lives = 1

letter = "s"

example_letter = "String word"

while lives > 0:
    if letter in example_letter.casefold():
        print("letter is in string")
    else:
        print("not in string")
    lives -= 1
    print(lives)

