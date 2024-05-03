#calculate Miles per gallon
import random
gallons_of_gas = random.randint(5, 20)
miles_travel_on_a_full_tank = random.randint(100,400)
MPG = miles_travel_on_a_full_tank//gallons_of_gas
print("Gallons of gas in the car's fuel: ",gallons_of_gas)
print("Miles it can travel on a full tank: ",miles_travel_on_a_full_tank)
print("MPG(miles per gallon): ",MPG)