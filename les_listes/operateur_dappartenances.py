utilisateurs = ["Michel","Karina","Joe","Melania"]
#1:verifier si nom existe 
# if "Melania" in utilisateurs:
#     print("Bonjour Melania, Bon retour parmis-nous")
# else:
#     print("tu n'existe pas")

#2:remove(""):pour effacer si un nom existe dans la liste
if "Melania" in utilisateurs:
   utilisateurs.remove("Melania")
print(utilisateurs)