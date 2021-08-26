
# listes caracteres special
# \a
exemple1  = "allo\aOuz"
print(exemple1)
# avec r
raw_exemple1  = r"allo\aOuz"
print(raw_exemple1)
# # # \b
# exemple2  = "allo\bOuz"
# print(exemple2)
# # avec r
# raw_exemple2  = r"allo\cOuz"
# print(raw_exemple2)
# # \f
# #sans raw
# exemple3  = "allo\fOuz"
# print(exemple3)
# #avec f
# raw_exemple3  = "allo\fOuz"
# print(exemple3)
# # \n
# exemple4  = "allo\fOuz"
# print(exemple4)
# # \r
# exemple5  = "allo\fOuz"
# print(exemple5)
# # \t
# exemple6  = "allo\fOuz"
# print(exemple6)
# # \v
# exemple7  = "allo\fOuz"
# print(exemple7)
# # chaines de caractere multilignes
print("""Il existe trois types numériques distincts: integers (entiers), floating point numbers (nombres flottants) et complex numbers (nombres complexes). En outre, les booléens sont un sous-type des entiers. Les entiers ont une précision illimitée. Les nombres à virgule flottante sont généralement implémentés en utilisant des double en C""")

# les raw strings
s = "Hi\nHello"
print(s)
raw_s = r"Hi\xBonjours" 
print(raw_s)
a = str(5)
print(type(a))
