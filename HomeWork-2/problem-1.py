# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class.
# Expected Output: Vehicle Name: School Volvo, Speed: 180, Mileage: 12

class Vehicle:
    def __init__(self, vehicle_name, speed, milage):
        self.vehicle_name = vehicle_name
        self.speed = speed
        self.milage = milage

    def vehicle_info(self):
        print("Vehicle Name: ",self.vehicle_name)
        print("Speed: ",self.speed)
        print("Milage: ",self.milage)

class Bus(Vehicle):
    def __init__(self, vehicle_name, speed, milage):
        super().__init__(vehicle_name,speed,milage)


x = Bus("School Volvo", 180, 12)

x.vehicle_info()


