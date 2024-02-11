class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_description_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def __str__(self):
        return self.get_description_name()
    
    def __repr__(self):
        return "Car Instance: " +  self.get_description_name()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspect of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        """Then initialize attributes specific to an electric car"""
        super().__init__(make, model, year)
        self.battery_size = 75
     
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")