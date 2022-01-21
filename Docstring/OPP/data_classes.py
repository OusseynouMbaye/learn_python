from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str = ""



emile = User("Emile", "Diop")
print(User.__dict__)
