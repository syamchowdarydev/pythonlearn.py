# Function to calculate Simple Interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Function to calculate Compound Interest
def calculate_compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return amount - principal

# Taking user input
principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of Interest (%): "))
time = float(input("Enter the Time (in years): "))

# Calculations
simple_interest = calculate_simple_interest(principal, rate, time)
compound_interest = calculate_compound_interest(principal, rate, time)

# Displaying results
print("\n--- Interest Calculations ---")
print(f"Simple Interest: ₹{simple_interest:.2f}")
print(f"Compound Interest: ₹{compound_interest:.2f}")
