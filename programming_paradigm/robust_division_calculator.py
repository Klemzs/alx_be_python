def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den
        return f"Result: {result}"
    
    except ZeroDivisionError:
        return "\nError: Zero division is not allowed"
    except ValueError:
        return "\nError: Please, enter only numeric values"

