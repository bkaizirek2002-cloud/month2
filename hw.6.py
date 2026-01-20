class Distance:
    conversion_dict = {
        'm': 1,
        'cm': 0.01,
        'km': 1000,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144,
        'mi': 1609.344
    }

    def __init__(self, value, unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")
        if unit not in self.conversion_dict:
            raise ValueError(f"Неизвестная единица измерения: {unit}")

        self.value = value
        self.unit = unit

    def convert_to_meters(self):
        return self.value * self.conversion_dict[self.unit]

    def convert_from_meters(self, meters, target_unit):
        if target_unit not in self.conversion_dict:
            raise ValueError(f"Неизвестная единица измерения: {target_unit}")
        return meters / self.conversion_dict[target_unit]

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __add__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Можно складывать только экземпляры Distance")

        total_meters = self.convert_to_meters() + other.convert_to_meters()
        total_value = self.convert_from_meters(total_meters, self.unit)

        return Distance(total_value, self.unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Можно вычитать только экземпляры Distance")

        diff_meters = self.convert_to_meters() - other.convert_to_meters()

        if diff_meters < 0:
            raise ValueError("Результат вычитания не может быть отрицательным")

        diff_value = self.convert_from_meters(diff_meters, self.unit)
        return Distance(diff_value, self.unit)

    def __eq__(self, other):
        if not isinstance(other, Distance):
            return False
        return self.convert_to_meters() == other.convert_to_meters()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Сравнение возможно только с экземплярами Distance")
        return self.convert_to_meters() < other.convert_to_meters()

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Сравнение возможно только с экземплярами Distance")
        return self.convert_to_meters() > other.convert_to_meters()

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


if __name__ == "__main__":
    d1 = Distance(10, 'm')
    d2 = Distance(2, 'km')
    d3 = Distance(500, 'cm')
    d4 = Distance(1, 'mi')

    print("Тестирование инициализации и __str__:")
    print(d1)
    print(d2)
    print(d3)
    print(d4)

    print("\nТестирование сложения:")
    result_add = d1 + d2
    print(f"{d1} + {d2} = {result_add}")  # 10 m + 2 km = 2010.0 m

    result_add2 = d3 + d1
    print(f"{d3} + {d1} = {result_add2}")  # 500 cm + 10 m = 15.0 m

    print("\nТестирование вычитания:")
    result_sub = d2 - d1
    print(f"{d2} - {d1} = {result_sub}")  # 2 km - 10 m = 1990.0 m

    try:
        result_sub2 = d1 - d2
        print(f"{d1} - {d2} = {result_sub2}")
    except ValueError as e:
        print(f"Ошибка при вычитании: {e}")

    print("\nТестирование сравнений:")
    print(f"{d1} == {d3}: {d1 == d3}")
    print(f"{d1} > {d3}: {d1 > d3}")
    print(f"{d2} >= {d4}: {d2 >= d4}")
    print(f"{d3} < {d1}: {d3 < d1}")
    print(f"{d1} != {d2}: {d1 != d2}")