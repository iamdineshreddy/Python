import math

try:
    num = float(input("Enter a number: "))

    if num <= 0:
        print("Please enter a positive number for square root and logarithm.")
    else:
        sqrt_value = math.sqrt(num)
        log_value = math.log(num)
        sin_value = math.sin(num)

        print(f"Square root of {num} is: {sqrt_value}")
        print(f"Natural logarithm of {num} is: {log_value}")
        print(f"Sine of {num} (in radians) is: {sin_value}")

except ValueError:
    print("Invalid input! Please enter a valid number.")
