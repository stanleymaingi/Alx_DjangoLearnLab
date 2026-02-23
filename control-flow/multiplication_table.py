# Multiplication Table Generator

# Step 1: Ask the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Step 2: Generate and print the table using a for loop
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
