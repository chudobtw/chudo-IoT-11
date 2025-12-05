from enum import Enum


class Kind(Enum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"
    OTHER = "other"


class Pet:
    def __init__(self, name, breed, age, greetings, mass, kind: Kind):
        self.name = name
        self.breed = breed
        self.age = age
        self.greetings = greetings
        self.mass = mass
        self.kind = kind

    def is_polite(self):
        return "Hello" in self.greetings

    def get_age(self):
        return self.age


class Home:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def get_pets(self):
        return self.pets

    @staticmethod
    def are_friends(pet_list):
        friends = []
        for i in range(len(pet_list)):
            for j in range(i + 1, len(pet_list)):
                if abs(pet_list[i].age - pet_list[j].age) < 2:
                    friends.append((pet_list[i], pet_list[j]))
        return friends
    
    @staticmethod
    def sort_by_age(pet_list):
        return sorted(pet_list, key=Pet.get_age)


p1 = Pet("Tsigan", "Black", 5, "Hello, friend!", 20.5, Kind.DOG)
p2 = Pet("Margo", "Siamic", 4, "Meow!", 4.2, Kind.CAT)
p3 = Pet("Guts", "Green", 2, "Hello mi frendo!", 0.8, Kind.BIRD)

home = Home()
home.add_pet(p1)
home.add_pet(p2)
home.add_pet(p3)

print("Хто тут чемний?:")
for p in home.get_pets():
    print(f"{p.name}, ти чемний(-на)? {p.is_polite()}")

print("\nДружні пари:")
for a, b in home.are_friends(home.get_pets()):
    print(f"{a.name} і {b.name}")

print("\nВідсортований список:")
for p in home.sort_by_age(home.get_pets()):
    print(p.name, p.age)
