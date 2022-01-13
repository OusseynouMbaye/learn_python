#replace
a = "bonjour , moi".replace(",","je suis").replace("jour", "soir")
# print(a)

#strip : efface les caracters(espace) du debut et la fin 
b = "    bonjour , moi   ".strip()
print(b)

#rstrip : efface les caracters de la partie droite
c = " bonjour , moi ".rstrip(" joi")
# print(c)

#lstrip : efface les caracters de la partie gauche
d = " bonjour , moi ".lstrip(" boj")
# print(d)