from datetime import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        education_status = "есть" if self.__higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.__occupation}. У меня {education_status} высшее образование.")



class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        education_status = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Я учился с Айсулуу в группе {self.group}. У меня {education_status} высшее образование.")



class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        education_status = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Моё хобби {self.hobby}. У меня {education_status} высшее образование.")

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = datetime.strptime(birth_date, "%d.%m.%Y")  # приватный атрибут
        self.__occupation = occupation  # приватный атрибут
        self.__higher_education = higher_education  # приватный атрибут

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    @property
    def age(self):
        today = datetime.today()
        return today.year - self.__birth_date.year - (
            (today.month, today.day) < (self.__birth_date.month, self.__birth_date.day)
        )

    def introduce(self):
        education_status = "есть" if self.__higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.__occupation}. У меня {education_status} высшее образование.")



class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        education_status = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Я учился с Айсулуу в группе {self.group}. У меня {education_status} высшее образование.")



class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        education_status = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Моё хобби {self.hobby}. У меня {education_status} высшее образование.")


cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()
print(cl1.age)

fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()
print(fr1.age)
import random

class Passenger:
    def __init__(self, current_floor, destination_floor):
        self.current_floor = current_floor
        self.destination_floor = destination_floor

    def __str__(self):
        return f"Пассажир (с {self.current_floor} на {self.destination_floor})"



class Elevator:
    def __init__(self, total_floors, max_capacity=5):
        self.total_floors = total_floors
        self.max_capacity = max_capacity
        self.current_floor = 1
        self.direction = "вверх"
        self.passengers = []
        self.floors_with_passengers = {}

    def add_passenger(self, passenger):
        if passenger.current_floor not in self.floors_with_passengers:
            self.floors_with_passengers[passenger.current_floor] = []
        self.floors_with_passengers[passenger.current_floor].append(passenger)

    def move(self):
        if self.direction == "вверх":
            self.current_floor += 1
            if self.current_floor == self.total_floors:
                self.direction = "вниз"
        else:
            self.current_floor -= 1
            if self.current_floor == 1:
                self.direction = "вверх"

    def pick_up_passengers(self):
        if self.current_floor in self.floors_with_passengers:
            available_space = self.max_capacity - len(self.passengers)
            picked_passengers = 0

            for passenger in self.floors_with_passengers[self.current_floor][:]:
                if (self.direction == "вверх" and passenger.destination_floor > self.current_floor) or \
                   (self.direction == "вниз" and passenger.destination_floor < self.current_floor):

                    if picked_passengers < available_space:
                        self.passengers.append(passenger)
                        self.floors_with_passengers[self.current_floor].remove(passenger)
                        picked_passengers += 1
                        print(f"Посадил {passenger} на {self.current_floor} этаже.")

    def drop_off_passengers(self):
        for passenger in self.passengers[:]:
            if passenger.destination_floor == self.current_floor:
                self.passengers.remove(passenger)
                print(f"Высадил {passenger} на {self.current_floor} этаже.")

    def show_status(self):
        passengers_count = len(self.passengers)
        print(f"Этаж: {self.current_floor}, "
              f"Пассажиров в лифте: {passengers_count}, "
              f"Направление: {self.direction}")

    def run_simulation(self, steps=20):
        for floor in range(1, self.total_floors + 1):
            num_passengers = random.randint(0, 3)
            for _ in range(num_passengers):
                dest = random.randint(1, self.total_floors)
                if dest != floor:
                    self.add_passenger(Passenger(floor, dest))