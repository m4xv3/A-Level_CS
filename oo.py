class Person():
    def __init__(self, name, age, height, eyecolour, hair):
        self.name = name
        self.age = int(age)
        self.height = float(height)
        self.eyecolour = eyecolour
        self.hair = hair
        self.jumpingstate = False
        self.sittingstate = False
        self.speakingstate = False
        self.runningstate = False
    def jump(self):
        print("I'm jumping")
        self.jumpingstate = True
        self.jumpingstate = False
    def sit(self):
        print("I'm sitting")
        self.sittingstate = True
    def speak(self):
        print("I'm speaking")
        self.speakingstate = True
    def run(self):
        print("I'm running")
        self.runningstate = True

class Student(Person):
    pass

person = Person("Jerome", 18, 210, "Green", "Black")

class Pet():
    def __init__(self, name, age, colour):
        self.__name = name
        self.age = age
        self.colour = colour
    def speak():
        print("Woof")

    def __str__(self):
        return f" Your pet is called {self.name}, and is {self.age} years old, and is {self.colour}"
    
    def getName(self):
        return self.__name

class Dog(Pet):
    def __init__(self, name, age, colour):
        super().__init__(name, age, colour)
        self.slippers = 0

    def Chew_Slipper(self, num):
        self.clippers += num

    

pet = Pet("Gerbert", 35, "Black")
pet = Dog("Gerbert", 35, "Black")
print(pet.getName())