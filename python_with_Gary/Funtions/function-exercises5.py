
def create_file(text, filename):
    with open(filename, 'w') as text_file:
        text_file.write(f"<p>{text}</p>")
        pass


create_file('allo comment ca va', 'hello2.html')
