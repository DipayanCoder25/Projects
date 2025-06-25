class BMW:
    def fuel_type(self):
        print("BMW uses Petrol")

    def max_speed(self):
        print("BMW max speed is 250 km/h")

class Ferrari:
    def fuel_type(self):
        print("Ferrari uses High-Octane Petrol")

    def max_speed(self):
        print("Ferrari max speed is 340 km/h")


def car_info(car):
    car.fuel_type()
    car.max_speed()

bmw_car = BMW()
ferrari_car = Ferrari()

car_info(bmw_car)

car_info(ferrari_car)
