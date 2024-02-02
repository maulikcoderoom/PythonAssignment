class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Mammal(Animal):
    def give_birth(self):
        return "Live birth"

class Dog(Mammal):
    def speak(self):
        return "Woof!"

class Color: 
    def __init__(self,color):
        self.color=color

class Cat(Animal, Color):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        Color.__init__(self, color)
    
    def speak(self):
        return "Meow!"

dog = Dog("Tom")
print(dog.name)  
print(dog.speak())  
print(dog.give_birth())  

cat = Cat("Whisker")
print(cat.speak())