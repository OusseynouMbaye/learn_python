import json
import logging
import os

from constants import DATA_DIR

LOGGER = logging.getLogger()


class Liste(list):
    def __init__(self, name):
        self.name = name

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que "
                             "des chaine de caractères !")

        if element in self:
            LOGGER.error(f"{element} est déjà dans la liste. ")
            return False

        self.append(element)
        return True

    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False

    def show(self):
        print(f"Ma liste de {self.name} : ")
        for element in self:
            print(f" - {element}")

    def save(self):
        chemin = os.path.join(DATA_DIR, f"{self.name}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        with open(chemin, "w") as f:
            json.dump(self, f, indent=4)

        return True


if __name__ == "__main__":
    liste = Liste("courses")
    liste.ajouter("Pommes")
    liste.ajouter("Poires")
    liste.save()