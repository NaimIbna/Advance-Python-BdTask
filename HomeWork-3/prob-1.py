class Animal():
    def sleep(self):
        print("I might sleep in different position with different attitudes")
    
    def eat(self):
        print("I eat to survive")
    
    def height(self):
        print("Based on my species characteristics I've different heights")

class Dog(Animal):
    def sleep(self):
        print("I sleep ")
    
    def eat(self):
        print("I eat to survive")
    
    def height(self):
        print("Based on my species characteristics I've different heights")

    def info(self):
        print("My name is Pogo")

class Horse(Animal):
    def sleep(self):
        print("I sleep in standing position")
    
    def eat(self):
        print("I eat hay or pasture to survive")
    
    def height(self):
        print("Based on my species characteristics I've different heights")

    def vision(self):
        print("I've nearly 360 degree field of vision")

class Snake(Animal):
    def sleep(self):
        print("I sleep while lying down")
    
    def eat(self):
        print("I eat to survive")
    
    def height(self):
        print("Based on my species characteristics I've different heights")

animal = Animal()
animal.eat()

print("------------------------")

dog = Dog()
dog.sleep()
dog.info()


print("------------------------")

horse = Horse()
horse.vision()


print("------------------------")

snake = Snake()
snake.sleep()


