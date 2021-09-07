# Create a function called ‘conversion’ that accepts one float argument, fahrenheit
# Convert temperature in Fahrenheit to Celsius using a formula (you can look up the conversion formula)
# Create a float variable to store the temperature in Celsius
# Print "[temperature]F can be converted to [temperature]C."
# If you are feeling up to it, have your function be able to convert from Celsius to Fahrenheit as well!  :D

#####################################

# Create a function called ‘sphere_volume’ that accepts one float argument, radius
# Calculate the volume of a sphere with that radius
# Return the volume as a float

#####################################

# Create a function called ‘factorial’ that accepts one integer argument, num.
# If num is not a positive number, return None.
# Otherwise, return the factorial of num (the product of all whole numbers starting at 1 and ending at x).
# E.g. the factorial of 3 is 3 * 2 * 1, which equals 6
# The factorial of 0 is 1

#####################################

import math as m


def conversion(degrees: float = 0.0, fahrenheit: bool = True) -> float:
    """
    Converts a number of degrees in either Fahrenheit or Celsius to the other scale, and prints the result.
    :param degrees: A number of degrees.
    :param fahrenheit: Whether the given number of degrees is in Fahrenheit or Celsius. True if Fahrenheit,
        False if Celsius. Defaults to True.
    :return: The result.
    """
    if fahrenheit:
        result: float = (degrees - 32) * 5 / 9
        print(str(degrees) + "\u00B0F can be converted to " + str(result) + "\u00B0C.")
    else:
        result: float = (degrees * 9 / 5) + 32
        print(str(degrees) + "\u00B0C can be converted to " + str(result) + "\u00B0F.")
    return result


def sphere_volume(radius: float) -> float:
    """
    Calculates the volume of a sphere given the radius.
    :param radius: The radius of the sphere.
    :return: The volume of the sphere.
    """
    return (4 / 3) * m.pi * (radius ** 3)


def factorial(num: int):
    """
    Calculates the factorial of a given positive integer.
    :param num: A positive integer to find the factorial of.
    :return: The factorial of the given positive integer.
    """
    if num < 0:
        return None
    num_f: int = 1
    for i in range(1, num+1):
        num_f *= i
    return num_f


def main():
    conversion(degrees=20.0, fahrenheit=False)
    r: float = 1.0  # example
    print("Volume of a sphere with radius " + str(r) + ": " + str(sphere_volume(radius=r)))
    n: int = 3  # example
    print("Factorial of " + str(n) + " is " + str(factorial(n)) + ".")


if __name__ == "__main__":
    main()
