import math

def triangle():
    print("\n--- Triangle ---")
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    # Check if valid triangle
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        s = perimeter / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Heron's Formula
        print(f"Perimeter of triangle: {perimeter}")
        print(f"Area of triangle: {area}")
    else:
        print("Not a valid triangle!")

def square():
    print("\n--- Square ---")
    side = float(input("Enter side length: "))
    perimeter = 4 * side
    area = side * side
    print(f"Perimeter of square: {perimeter}")
    print(f"Area of square: {area}")

def rectangle():
    print("\n--- Rectangle ---")
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    perimeter = 2 * (length + width)
    area = length * width
    print(f"Perimeter of rectangle: {perimeter}")
    print(f"Area of rectangle: {area}")

# Menu
while True:
    print("\nChoose a shape to calculate:")
    print("1. Triangle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        triangle()
    elif choice == "2":
        square()
    elif choice == "3":
        rectangle()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
