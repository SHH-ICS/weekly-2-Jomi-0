import sys
import math

def calculate_area(radius):
    return math.pi * float(radius) ** 2

def calculate_circumference(radius):
    return 2 * math.pi * float(radius)

if __name__ == "__main__":
    radius = sys.argv[1]
    calc_type = sys.argv[2]

    if calc_type == 'area':
        result = calculate_area(radius)
    elif calc_type == 'circumference':
        result = calculate_circumference(radius)
    
    print(result)

