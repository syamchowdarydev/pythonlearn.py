import math

# Triangle
print("\n--- Triangle ---")
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
side1 = float(input("Enter side 1 of triangle: "))
side2 = float(input("Enter side 2 of triangle: "))
side3 = float(input("Enter side 3 of triangle: "))

triangle_area = 0.5 * base * height
triangle_perimeter = side1 + side2 + side3

print(f"Area of triangle: {triangle_area}")
print(f"Perimeter of triangle: {triangle_perimeter}")

# Rectangle
print("\n--- Rectangle ---")
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)

print(f"Area of rectangle: {rectangle_area}")
print(f"Perimeter of rectangle: {rectangle_perimeter}")

# Square
print("\n--- Square ---")
side = float(input("Enter side of square: "))

square_area = side * side
square_perimeter = 4 * side

print(f"Area of square: {square_area}")
print(f"Perimeter of square: {square_perimeter}")

# Circle
print("\n--- Circle ---")
radius = float(input("Enter radius of circle: "))

circle_area = math.pi * radius ** 2
circle_perimeter = 2 * math.pi * radius

print(f"Area of circle: {circle_area}")
print(f"Circumference of circle: {circle_perimeter}")
