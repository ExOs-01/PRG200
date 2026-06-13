# Temperature Logger (math module)

import math

station_name = "Kathmandu Weather Station"    

temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]

def get_average(temps):
    total = 0
    for t in temps:
        total = total + t
    return total / len(temps)

def get_deviation(temps):
    mean = get_average(temps)    
    total = 0
    for t in temps:
        total = total + (t - mean) ** 2
    variance = total / len(temps)
    return math.sqrt(variance)

def get_summary(temps):
    print(f"Station: {station_name}")
    print(f"Min Temperature  : {min(temps)} C")
    print(f"Max Temperature  : {max(temps)} C")
    print(f"Average          : {get_average(temps):.2f} C")
    print(f"Std Deviation    : {get_deviation(temps):.2f} C")

get_summary(temperatures)

# Trying to access the local variable 'mean' from outside get_deviation() causes a NameError
# because 'mean' only exists inside get_deviation(), it is destroyed when the function ends
# print(mean)   # NameError: name 'mean' is not defined