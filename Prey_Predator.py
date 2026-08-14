class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
class Rabbit(Prey):         #inherits all methods of Animal and Prey
    pass
class Snake(Predator,Prey): #inherits all methods of Animal, Prey, Predatoer
    pass
snake=Snake("Kaa")
snake.hunt()
rabbit=Rabbit("Bugs")
rabbit.sleep()

