def count_occurences(text, word):
    return text.lower().split().count(word)


message = "python this python Python is popular programming language"

word = "python"
count = count_occurences(message, word)
print(f"Le word {word} appears {count} dans le texte : {message}")
