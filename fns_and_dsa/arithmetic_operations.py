# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations.

    Parameters:
        num1 (float): The first number
        num2 (float): The second number
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'

    Returns:
        float or str: Result of the operation, or an error message for division by zero
    """
    operation = operation.strip().lower()  # normalize input

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"  # Handle division by zero
        return num1 / num2
    else:
        return "Error: Invalid operation"
