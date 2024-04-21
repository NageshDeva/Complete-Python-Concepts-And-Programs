#Hybrid Inheritance
'''
The process of combining more than one type of inheritance
together while deriving sub classes in a program is called
Hybrid Inheritance.
'''
class Animal:
    def __init__(self, species):
        self.species = species

    def eat(self):
        print("Animal is eating")

class Mammal(Animal):
    def __init__(self, species, legs):
        super().__init__(species)
        self.legs = legs

    def walk(self):
        print("Mammal is walking")

class Bird(Animal):
    def __init__(self, species, wings):
        super().__init__(species)
        self.wings = wings

    def fly(self):
        print("Bird is flying")

class Bat(Bird, Mammal):  # Hybrid inheritance
    def __init__(self, species, legs, wings):
        
        super().__init__(species, legs)
        Bird.__init__(self, species, wings)
        

    def fly(self):  # Overriding fly method
        print("Bat is flying")

    def walk(self):  # Overriding walk method
        print("Bat is walking")

# Creating an instance of Bat
bat = Bat("Bat", 2, 2)

# Accessing attributes and calling methods
print("Species:", bat.species)
print("Legs:", bat.legs)
print("Wings:", bat.wings)
bat.eat()  # Inherited from Animal class
bat.walk()  # Overridden method from Mammal class
bat.fly()  # Overridden method from Bat class
