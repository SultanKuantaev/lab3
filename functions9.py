import math

radius = int(input("Enter the radius: "))

def volume(radius):
    return (4/3) * math.pi * (radius**3)

print(volume(radius))
