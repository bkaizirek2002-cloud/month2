class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if isinstance(name, str) and len(name.strip()) > 0:
            self.__name = name.strip()
        else:
            raise ValueError("Имя должен быть непустой строкой")

    def set_age(self, age):
        if isinstance(age, int) and age >=0:
            self.__age = age
        else:
            raise ValueError("Возраст должен быть неотрицательным целым числом")

    def make_sound(self):
        raise NotImplementedError("Метод make_sound() должен быть переопределён в подклассе")


class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу-мяу"

if __name__ == "__main__":
    dog =Dog("Бобик",3)
    cat = Cat("Мурка",2)

    print(f"{dog.get_name()} говорит: {dog.make_sound()}")
    print(f"{cat.get_name()} говорит: {cat.make_sound()}")

    dog.set_name("Шарик")
    dog.set_age(9)

    cat.set_name("Ириска")
    cat.set_age(6)

    print(f"Теперь собака - {dog.get_name()}, возраст: {dog.get_age()}лет")
    print(f"Теперь кошка - {cat.get_name()}, возраст:{cat.get_age()}лет")