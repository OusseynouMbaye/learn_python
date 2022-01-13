from pathlib import Path

"""
Trier les fichiers contenus dans le dossier data selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
"""
EXTENSIONS_MAPPING = {".mp3": "Musique",
                      ".wav": "Musique",
                      ".flac": "Musique",
                      ".avi": "Videos",
                      ".mp4": "Videos",
                      ".bmp": "Images",
                      ".png": "Images",
                      ".jpg": "Images",
                      ".txt": "Documents",
                      ".pptx": "Documents",
                      ".csv": "Documents",
                      ".xls": "Documents",
                      ".odp": "Documents",
                      ".pages": "Documents",
                      }
file_parent = Path.cwd()  # afficher le dossier courant

BASE_DIR = file_parent / "data"  # concatenate le dossier courant avec data
# Autre methode pour base dire
# BASE_DIR = Path('C:\Users\Ouzinem\Desktop\onlineCourse\learn_python\Exercises\Trieur_files\data')
files = [filename for filename in BASE_DIR.iterdir() if filename.is_file()]  # recuperation des fichiers
for file in files:
    target_folder = EXTENSIONS_MAPPING.get(file.suffix, "Divers")
    dossier_cible_absolu = BASE_DIR / target_folder
    dossier_cible_absolu.mkdir(exist_ok=True)  # 1 create les dossier Musique, Documents, Images
    target_file = dossier_cible_absolu / file.name
    file.rename(target_file)  # deplacer les fichier dans leurs dossier
