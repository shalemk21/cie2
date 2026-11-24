def celsius_to_fahrenheit(celsisus):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
c=float(input("Enter temperature in Celsius: "))
f=celsius_to_fahrenheit(c)
print("temperature in Fahrenheit:", f)