# Parent Class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        return f"The {self.brand} {self.model} is now ON."

    def turn_off(self):
        return f"The {self.brand} {self.model} is now OFF."

# Child Class: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model)  # Initialize parent class attributes
        self.storage = storage
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        return f"Taking a photo with the {self.camera_megapixels}MP camera."

    def install_app(self, app_name):
        return f"Installing {app_name} on {self.brand} {self.model}."

# Create objects
phone1 = Smartphone("Apple", "iPhone 14", "128GB", 12)
phone2 = Smartphone("Samsung", "Galaxy S22", "256GB", 50)

# Interact with the objects
print(phone1.turn_on())
print(phone1.take_photo())
print(phone2.install_app("WhatsApp"))
print(phone2.turn_off())


#Activity 2 

 #Parent Class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        return "The car is driving 🚗."

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "The plane is flying ✈️."

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return "The boat is sailing 🚢."

# Create objects
car = Car()
plane = Plane()
boat = Boat()

# Polymorphism in action
vehicles = [car, plane, boat]
for vehicle in vehicles:
    print(vehicle.move())