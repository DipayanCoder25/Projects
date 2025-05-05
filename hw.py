import math

def calculate_circumference(radius):
   
    circumference = 2 * math.pi * radius
    return circumference


r = float(input("Enter the radius of the circle: "))
result = calculate_circumference(r)
print(f"The circumference of the circle is: {result}")
