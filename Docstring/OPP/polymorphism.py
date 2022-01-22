class Vehicule:
    def avance(self):
        print("Le vehicule avance")


class Voiture(Vehicule):
    def avance(self):
        super().avance()
        print("La voiture avance")


class Avion(Vehicule):
    def avance(self):
        super().avance()
        print("L'avion vol")


v = Voiture()
a = Avion()
v.avance()
a.avance()