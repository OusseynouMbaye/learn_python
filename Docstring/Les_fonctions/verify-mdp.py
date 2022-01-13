
mdp = input("Entrez un mot de passe (min 8 caracteres) : ")
mdp_trop_court = "Votre mdp est tro court"
mdp_contient = "Votre mdp contient que des nombres"

if len(mdp) == 0:
    print(mdp_trop_court.capitalize())
elif not len(mdp) > 8:
    print(mdp_trop_court.upper())
elif mdp.isdigit():
    print(mdp_contient.capitalize())
else:
    print("inscription done")
