from tkinter.font import names


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

carOne = Car("red", 1200)
carTwo = Car("blue", 10)

print(carOne, carTwo)

class Animal:
    def __init__(self, species):
        self.species = species
    def typeOfAnimal(self):
        return "I am a " + self.species + "type of animal"

class Dog(Animal):
    def __init__(self, species, color, breed):
        super().__init__(species)
        self.species = species
        self.color = color
        self.breed = breed

goldrenRetriver = Dog(species="Dog", color="golden", breed="golden retriever")