import json

file = "settings.json"

with open(file, 'r') as file_name:
    settings = json.load(file_name)  # module json pour recuperer le contenu

# print(settings.get("fontSize"))

# pour modifier des donnee dans le fichier json
settings["fontSize"] = 25  # modfiier la valeur de fontSize
settings["color"] = "red"  # ajouter color

with open(file, 'w') as file_name:
    json.dump(settings, file_name, indent=4)
