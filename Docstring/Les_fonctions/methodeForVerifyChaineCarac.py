a = "aLlo"

print(a.isdigit())

b = "500"

#isdigit methode tres populaire
print(b.isdigit())
#count permet de compter le nombre de fois un mot se trouve dans une phrase
c = "Il est presque l'heure. il doi. il"
print(c.count("il"))

#find: indique la 1ere fois qu"il trouve le caractere recherche
#rfind:recherhe a partir de la droite (existe pas lfind)
d = "Il est presque l'heure. il doi. il"
print(d.find("e"))
#index: indique la 1ere fois qu"il trouve le caractere recherche
z = "Il est presque l'heure. il doi. il"
print(z.index("e"))
#index et find font la meme chose  
#la difference est que avec find si il ne troupe la caractere il retourne -1 et index lui le prgramme leve une Error

#endswith
t = "image.png".endswith(".png")
print(t)