import random
print("**** function rand int*****")
#function randint :genere un nbre entier aleatoir
a =  random.randint(1,6)
print("a : ",a)
print("**** function uniform*****")
#function uniform: genere un nbre decimal aleatoire
b =  random.uniform(0, 1)
print("b : ",b)

print("**** function  rand range*****")
#function rand range : permet de specifier un pas aleatoire
c =  random.randrange(0,12,2)
print("c : ",c)