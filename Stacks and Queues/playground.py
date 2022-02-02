import enum

class Animal(enum.Enum):
    dog = 1
    cat = 2

test = Animal.dog
print(test.name)