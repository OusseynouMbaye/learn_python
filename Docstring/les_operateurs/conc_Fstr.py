# f-string est la meilleur methode pour ecrire un texte avec du code
from typing import Protocol


a = 10
# print(type(a))
print(f"j'ai {a} ans")

a = 10
b = 4
c = 12
phrase = "j'ai {2} et toi tu {0} et il est {0} h".format(b, a, c)
# print(type(a))
print(phrase)

# 3 facons de faire

protocole = "https://"
nom_du_site = "Ouzinem"
extension = "com"
# #avec l'operateur
url1 = protocole + "www." + nom_du_site + "." + extension
print(url1)
# #avec format
url2 = ("{0}www.{1}.{2}").format(protocole,nom_du_site,extension)
url3 =("{}www.{}.{}").format(protocole,nom_du_site,extension)
print(url2)
print(url3)
# #avec f-string
url = f"{protocole}www.{nom_du_site}.{extension}"
print(url)
