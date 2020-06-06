# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    pass

class GroundVehicle(Vehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

class FlightVehicle(Vehicle):
    pass

class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass
# This is the base class
# class Vehicle:
#     def __init__(self, vehicle_name, is_Flight = False, is_Star = False):
#         self.vehicle_name = vehicle_name
#         self.is_Flight = is_Flight
#         self.is_Star = is_Star
#     pass

# class GroundVehicle(Vehicle):
#     def __init__(self, vehicle_name):
#         super().__init__(vehicle_name)
#         pass
#     pass

# class Car(GroundVehicle):
#     def __init__(self, vehicle_name):
#         super().__init__(vehicle_name)
#         pass
#     pass

# class Motorcycle(GroundVehicle):
#     def __init__(self, vehicle_name):
#         super().__init__(vehicle_name)
#         pass
#     pass

# class FlightVehicle(Vehicle):
#     def __init__(self, vehicle_name):
#         super().__init__(vehicle_name, is_Flight = True) 
#         pass
#     pass

# class Airplane(FlightVehicle):
#     def __init__(self, vehicle_name):
#         super().__init__(vehicle_name)
#         pass
#     pass

# class Starship(Vehicle):
#     def __init__(self, vehicle_name): 
#         super().__init__(vehicle_name, is_Star = True)
#         pass
# class Starship(FlightVehicle):
#     pass
