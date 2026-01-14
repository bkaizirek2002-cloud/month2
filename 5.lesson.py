class Animal:
    def move(self):
        print('двигается')

class Swimming(Animal):
    def move(self):
        print('плавает')

class Flying(Animal):
    def move(self):
        print('летает')

class Duck(Flying, Swimming):
    def move(self):
        super().move()
        print('летает и плавает')

#MRO = method resolution order
print(Duck.__mro__)
duck = Duck()
duck.move()

print("======")
print(Swimming.__mro__)
animal = Swimming()
animal.move()