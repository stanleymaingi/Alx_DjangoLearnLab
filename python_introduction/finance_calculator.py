# Personal Finance Calculator

# Step 1: Get user input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Step 2: Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Step 3: Calculate projected annual savings with interest
interest_rate = 0.05  # 5% annual interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)

# Step 4: Display results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
