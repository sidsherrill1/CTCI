class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, pet):
        Person.__init__(self, name, age)
        self.pet = pet


sidney = Student("Sid", 29, "Roxie")
print(sidney.name)
print(sidney.pet)
