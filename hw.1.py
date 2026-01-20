class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        if self.higher_education:
            edu_status = "имею высшее образование"
        else:
            edu_status = "высшего образования нет"
        return f"Меня зовут {self.name}, родилась {self.birth_date}, Моя профессия {self.occupation}, Я {edu_status}"

person1 = Person(name="Айзирек", birth_date="05.08.2002", occupation="Переводчик", higher_education=False)
person2 = Person(name="Ислам", birth_date="13.12.2001", occupation="Фрилансер", higher_education=True)
person3 = Person(name="Айнука", birth_date="25.07.2000", occupation="Менеджер", higher_education=False)

# Выводим результаты
print(person1.introduce())
print(person2.introduce())
print(person3.introduce())
