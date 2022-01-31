groups = ["group_2x", "group_3x", "local"]


class User:
    def __init__(self, name, prenom):
        self.name = name
        self.prenom = prenom

    def __str__(self):
        return f"Utilisateur {self.name} {self.prenom}"

    @staticmethod
    def show_group():
        for group in groups:
            print(group)


class Competitor(User):
    def __init__(self, name, prenom):
        super().__init__(name, prenom)

    @staticmethod
    def show_group():
        for group in groups:
            if "x" in group:
                print(group)


eve = Competitor("eve", "lacasse")
print(eve)
eve.show_group()
