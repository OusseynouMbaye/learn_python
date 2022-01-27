class User:
    def __init__(self, id):
        self.id = id


class Admin(User):
    def __init__(self, id):
        super().__init__(id)

    def __repr__(self):
        return f'Admin(id={self.id})'


admin1 = Admin("1")


# print(admin1)

class Student:
    def __init__(self, name):
        self.name = name


class Class:
    def __init__(self, name):
        self.name = name
        self.students = set()

    def add_student(self, student):
        self.students.add(student)

    def __len__(self):
        return len(self.students)


student1 = Student('Emy')
student2 = Student('Alex')

maternelle = Class('Maternelle')

maternelle.add_student(student1)
maternelle.add_student(student2)

count_student = len(maternelle)

print(count_student)
