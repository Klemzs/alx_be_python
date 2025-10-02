def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "\nError: Cannot divide by zero."
    except ValueError:
        return "\nError: Please enter numeric values only."

