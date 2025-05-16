import math
import random

angle_deg = float(input("Enter angle in degrees: "))


angle_rad = math.radians(angle_deg)

sine_value = math.sin(angle_rad)
cosine_value = math.cos(angle_rad)
tangent_value = math.tan(angle_rad)

print(f"\nTrigonometric values for {angle_deg}°:")
print(f"sin({angle_deg}) = {sine_value}")
print(f"cos({angle_deg}) = {cosine_value}")
print(f"tan({angle_deg}) = {tangent_value}")
