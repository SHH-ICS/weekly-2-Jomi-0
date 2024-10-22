import math

def circle_calculator():
    radius = float(input("Enter the radius of the circle: "))
    area = round(math.pi * radius * radius, 2)
    circumference = round(2 * math.pi * radius, 2)
    
    print(f"Area: {area} square units")
    print(f"Circumference: {circumference} units")

if __name__ == "__main__":
    circle_calculator()

