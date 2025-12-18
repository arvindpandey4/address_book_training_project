from abc import ABC, abstractmethod


class FuelSystem(ABC):
    @abstractmethod
    def fuel(self, throttle, load, temperature):
        pass


class PetrolFuelSystem(FuelSystem):
    def fuel(self, throttle, load, temperature):
        base_flow = 0.8
        throttle_factor = throttle * 0.05
        load_factor = load * 0.1

        if temperature < 10:
            temp_factor = 1.2
        elif temperature > 40:
            temp_factor = 0.9
        else:
            temp_factor = 1.0

        injector_efficiency = 0.92
        combustion_loss = 0.08

        raw_fuel = base_flow + throttle_factor + load_factor
        adjusted_fuel = raw_fuel * temp_factor
        final_fuel = adjusted_fuel * injector_efficiency
        usable_fuel = final_fuel * (1 - combustion_loss)

        return f"Petrol supplied: {round(usable_fuel, 2)} units"


class DieselFuelSystem(FuelSystem):
    def fuel(self, throttle, load, temperature):
        base_pressure = 300
        throttle_pressure = throttle * 25
        load_pressure = load * 40

        total_pressure = base_pressure + throttle_pressure + load_pressure

        if temperature < 5:
            total_pressure += 50

        injection_timing = total_pressure * 0.002
        compression_efficiency = 0.88

        final_output = injection_timing * compression_efficiency

        return f"Diesel supplied: {round(final_output, 2)} units"


class Machinery:
    def __init__(self, fuel_type):
        if fuel_type == "petrol":
            self.fuel_system = PetrolFuelSystem()
        elif fuel_type == "diesel":
            self.fuel_system = DieselFuelSystem()
        else:
            raise ValueError("Invalid fuel type")

    def run(self):
        throttle = 6
        load = 4
        temperature = 25

        print(self.fuel_system.fuel(throttle, load, temperature))


machine1 = Machinery("petrol")
machine1.run()

machine2 = Machinery("diesel")
machine2.run()



#what can be done self.fuel_system.fuel(throttle, load, temperature)
#what cannot be done
#self.fuel_system.base_flow
#self.fuel_system.injector_efficiency
#self.fuel_system.total_pressure



# PetrolFuelSystem hides:

# base_flow
# throttle_factor
# load_factor
# temp_factor
# injector_efficiency
# combustion_loss


# DieselFuelSystem hides:

# base_pressure
# throttle_pressure
# load_pressure
# total_pressure
# injection_timing
# compression_efficiency