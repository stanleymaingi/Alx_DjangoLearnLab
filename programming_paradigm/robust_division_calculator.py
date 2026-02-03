def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with error handling.
    Returns the result or an error message.
    """
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        # Attempt division
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
