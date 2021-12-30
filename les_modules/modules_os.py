#module permet de creer et supprimer des dossiers ou fihcier
from genericpath import exists
import os

chemin = "/Users/iclic/Desktop/learn-python"
#creer un dossier on use os.path.join et os.makedirs
dossier = os.path.join(chemin, "dossier")
#creer un dossier avec makedirs
#Pour vaire une validation faire cette methode 1
#  if not os.path.exists(dossier):
#     os.makedirs(dossier)

#methode 2 
#os.makedirs(dossier2,exist_ok=True)
# print(dossier)

#supprimer un dossier :faire une verification pour voir si un dssier exist ou non
if os.path.exists(dossier):
    os.removedirs(dossier)