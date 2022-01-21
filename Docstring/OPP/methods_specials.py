class Swimmer:
    swimmer_cree = 0

    def __init__(self, name, age, specialty):
        Swimmer.swimmer_cree += 1
        self.name = name
        self.age = age
        self.specialty = specialty

    @classmethod
    def butterfly(cls):
        return cls(name="Samuelle", age="16", specialty="Butterfly")

    @classmethod
    def freestyle(cls):
        return cls(name="Ana", age="14", specialty="free")

    @staticmethod
    def number_swimmer():
        print(f"il y  {Swimmer.swimmer_cree} nageurs cree")

    def __str__(self):
        return f"{self.name} est age de {self.age} pour nage favorite {self.specialty}"


samuelle = Swimmer.butterfly()
ana = Swimmer.freestyle()
print(ana)
print(samuelle)
# Swimmer.number_swimmer()
