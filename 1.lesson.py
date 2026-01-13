class Car:
    #инициализатор
   def __init__(self, model, color):
        self.model = model
        self.color = color

car_subaru = Car("Subaru", "Red")
print(car_subaru)
print(car_subaru.model)
print(car_subaru.color)
print(type(car_subaru))


class Car:
    def __init__(self,model,color):
        self.model = model
        self.color = color



car_honda = Car("Honda", "black")
print(car_honda)
print(car_honda.model)
print(car_honda.color)
car_honda.drive_to("Karakol")
car_honda.change_color("Black")
print(type(car_honda))
