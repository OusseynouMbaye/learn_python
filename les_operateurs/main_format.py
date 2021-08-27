from constants import BONJOUR
#exemple pour utliser la methode format
user = input("Entrez votre nom d'utilisateur : ")
progression = get_weekly_progression(user)
msg_bienvenue =  BONJOUR.format(user, nombre_videos= progression)
print(msg_bienvenue)