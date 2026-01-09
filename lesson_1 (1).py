class Car:
    # ининциализатор
    def __init__(self,  model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def drive_to(self, destination):
        print(f"Car {self.model} Driving to", destination)

    def change_color(self, new_color):
        self.color = new_color


car_subaru = Car("Subaru", "red")
car_subaru1 = Car("Subaru", "red")
car_subaru2 = Car("Subaru", "red")
car_kia = Car("Kia", "silver")
print(car_subaru)
print(car_subaru1)
print(car_subaru2)
print(car_subaru.model)
print(car_subaru.color)
print(car_kia.color)
car_kia.drive_to("Karakol")
car_kia.change_color("black")
print(car_kia.color)
car_subaru.model = "Forester"
print(car_subaru.model)
car_subaru.max_speed = 140
print(car_subaru.max_speed)
# print(car_kia.max_speed) # Error такого атрибута нет у объектов класса
print(type(car_subaru))
print(type("fsdfsdfsd"))