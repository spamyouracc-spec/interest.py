def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit and return the result."""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius and return the result."""
    return (f - 32) * 5/9


if __name__ == "__main__":
    print(celsius_to_fahrenheit(25))
    print(fahrenheit_to_celsius(77))
