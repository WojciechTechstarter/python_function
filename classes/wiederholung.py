import math

class Vehicles:
    def __init__(
        self, vehicle_brand_name, vehicle_model_name, average_consumption_in_l, tank_size,
    ):
        self.brand_name = vehicle_brand_name
        self.model_name = vehicle_model_name
        self.consumption = average_consumption_in_l
        self.km_driven = 0
        self.tank = tank_size
        self.cost_per_km = 1.70

    def get_description(self):
        return self.brand_name + ", " + self.model_name

    def drive(self, km_driven):
        self.km_driven = self.km_driven + km_driven

    def get_total_consumption(self):
        cons_in_l_per_km = self.consumption / 100

        return cons_in_l_per_km * self.km_driven

    def get_number_of_refuel(self):
        coverage_with_one_tank = self.tank / self.consumption
        refuel = self.km_driven / self.consumption / self.tank

        return math.ceil(refuel)

    def get_total_cost(self):
        cost = self.km_driven * self.cost_per_km

        return cost


my_vehicle = Vehicles("VW", "Golf", 10, 100)
my_vehicle.drive(1000)
my_vehicle.drive(50)
my_vehicle.drive(4000)
my_vehicle.drive(1500)

print(f"Der gesamte Verbauch liegt bei: {my_vehicle.get_total_consumption()}")
print(f'You need to refuel the tank {my_vehicle.get_number_of_refuel()} times')
print(f'The ride costs {my_vehicle.get_total_cost} euro')