# Taking input from the user
num = int(input("Enter a number: "))

# Save the original number to compare later
original_num = num

# Initialize sum to 0
sum = 0

# Find the number of digits
num_digits = len(str(num))

# Calculate the sum of the digits raised to the power of number of digits
while num > 0:
    digit = num % 10            # Get the last digit
    sum += digit ** num_digits  # Add digit raised to power of num_digits
    num = num // 10             # Remove the last digit

# Check if the number is an Armstrong number
if sum == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")
