class Vehicle:
    def start(self):
        print("Vehicle starting")


class Car(Vehicle):
    def start(self):
        print("Car starting")
        super().start()


class ElectricCar(Vehicle):
    def start(self):
        print("Electric system online")
        super().start()


class Tesla(ElectricCar, Car):
    def start(self):
        print("Tesla booting")
        super().start()


if __name__ == "__main__":
    Tesla().start()

class BaseView:
    def render(self):
        print("Template render")


class LoggingMixin:
    def render(self):
        print("Log: start")
        super().render()
        print("Log: end")


class AuthRequiredMixin:
    def init(self, authed=True):
        self.authed = authed

    def render(self):
        if self.authed:
            print("Auth OK")
            super().render()
        else:
            print("Access denied")


class AdminPageView(LoggingMixin, AuthRequiredMixin, BaseView):
    def render(self):
        print("Admin page render start")
        super().render()
        print("Admin page render end")


if __name__ == "main":
    print("=== Authenticated ===")
    admin = AdminPageView(authed=True)
    admin.render()

    print("\n=== Not authenticated ===")
    guest = AdminPageView(authed=False)
    guest.render()