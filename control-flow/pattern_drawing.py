# Drawing a square pattern using nested loops

# Step 1: Get pattern size from user
size = int(input("Enter the size of the pattern: "))

# Step 2: Initialize row counter
row = 0

# Step 3: Draw the square pattern
while row < size:
    for col in range(size):
        print("*", end="")  # print '*' side by side
    print()  # move to next row
    row += 1  # increment row
