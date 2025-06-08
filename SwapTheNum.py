# Taking input from the user
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

print("\nprint swaping")
print("a= ",a,"b= ",b)

# 1. Swapping using a temporary variable
temp = a
a = b
b = temp
print("\nAfter swapping using temporary variable:")
print("a =", a, "b =", b)

# Resetting values
a = int(input("\nEnter the first number (a) again: "))
b = int(input("Enter the second number (b) again: "))

# 2. Swapping using tuple unpacking
a, b = b, a
print("\nAfter swapping using tuple unpacking:")
print("a =", a, "b =", b)

# Resetting values
a = int(input("\nEnter the first number (a) again: "))
b = int(input("Enter the second number (b) again: "))

# 3. Swapping using arithmetic operations
a = a + b
b = a - b
a = a - b
print("\nAfter swapping using arithmetic operations:")
print("a =", a, "b =", b)

# Resetting values
a = int(input("\nEnter the first number (a) again: "))
b = int(input("Enter the second number (b) again: "))

# 4. Swapping using XOR
a = a ^ b
b = a ^ b
a = a ^ b
print("\nAfter swapping using XOR bitwise operator:")
print("a =", a, "b =", b)
