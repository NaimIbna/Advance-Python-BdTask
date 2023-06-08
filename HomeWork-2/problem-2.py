# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. 
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        fare = self.seating_capacity*100
        return fare
    
class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    def fare_charge(self):
        total_fare = super().fare()
        final_amount = total_fare + (total_fare * 0.1)
        return final_amount
    
x = Bus(50)
#print(x.fare())

fare = x.fare_charge()
print(fare)
    
    