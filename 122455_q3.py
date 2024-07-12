	# Creating the Base Vehicle Class: We’ll start by defining a base Vehicle class with common attributes such as registration number, make, and model. Other vehicle types (cars, trucks, motorcycles) will inherit from this base class. Here’s an example implementation:
class Vehicle:
    def __init__(self, registration_number, make, model):
	    self.registration_number = registration_number
self.make = make
self.model = model
	
# Example usage:
vehicle1 = Vehicle("KAD234H", "Toyota", "Bluebird")

# Creating the Derived Classes: Next, we’ll create specific classes for Car, Truck, and Motorcycle, inheriting from the Vehicle class. Each derived class will have additional attributes specific to its type:

class Car(Vehicle):
      def __init__(self, registration_number, make, model, num_seats):
	        super().__init__(registration_number, make, model)
self.num_seats = num_seats
	
class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
	        super().__init__(registration_number, make, model)
self.cargo_capacity = cargo_capacity
	
class Motorcycle(Vehicle):
  def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
self.engine_capacity = engine_capacity

	# Example usage:
car1 = Car("KCQ345T", "Mercedes", "GLC", 5)
truck1 = Truck("KAP845P", "Ford", "Ranger", 2000)  # Cargo capacity in kg
motorcycle1 = Motorcycle("KBL297S", "NISSAN", "X-trail", 750)  # Engine capacity in cc

# Creating the Fleet Class: Now let’s create a Fleet class to manage the vehicles. We’ll add methods to add a vehicle, display all vehicles, and search by registration number:
class Fleet:
  def __init__(self):
	    self.vehicles = []  # Initialize an empty list for vehicles
	
def add_vehicle(self, vehicle):
	        """
	        Adds a vehicle to the fleet.
		        Args:
	            vehicle (Vehicle): An instance of the Vehicle class.
	
	        Returns:
	            None
        """
        self.vehicles.append(vehicle)
	
def display_all_vehicles(self):
        """
        Displays details of all vehicles in the fleet.
	
	        Returns:
            None
	        """
for vehicle in self.vehicles:
	 print(f"Registration: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}")
	
def search_by_registration(self, reg_number):
	        """
	        Searches for a vehicle by registration number and displays its details.
	
	        Args:
            reg_number (str): Registration number to search for.
	
	        Returns:
	            None
	        """
for vehicle in self.vehicles:
	            if vehicle.registration_number == reg_number:
	                print(f"Found vehicle: Make: {vehicle.make}, Model: {vehicle.model}")
	            return
print(f"No vehicle found with registration number '{reg_number}'.")
	
	# Example usage:
fleet = Fleet()
fleet.add_vehicle(car1)
fleet.add_vehicle(truck1)
fleet.add_vehicle(motorcycle1)
fleet.display_all_vehicles()
fleet.search_by_registration("KCA234J")  # Search for a specific registration number
