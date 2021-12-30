liste = [1,2,3,4,5]
print(liste)

# ajouter des elements a une liste
# methode append ajouter juste un element
liste.append(6)
print(liste)
# methode extend ajoute plusieur elements dans une liste
print("**** ajouter plusieur element dans une liste *****")
liste.extend([7,8])
print(liste)
print("**** recupere un element dans une liste *****")
print(liste[1])
print("**** slice *****")
print(liste[0:1]) #recupere l'element 1 du tableau
print(liste[0:2]) #recupere les deux premiers element du tableau
print(liste[:]) #recupere tout le tableau
print(liste[1:5:2]) #recupere un element a l'indice 1 avec un pas de 2
print(liste[1::2]) #recupere un element a l'indice 1 avec un pas de 2

# pour enlever un element 
# methode remove
print("**** effacer un element de la liste*****")
liste.remove(6)
print(liste)

print("**** inverse les element du taableau*****")
liste.reverse()
print(liste)
