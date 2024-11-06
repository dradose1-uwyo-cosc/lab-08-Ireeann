# Ireeann Anderson
# UWYO COSC 1010
# Submission Date
# Lab 08
# Lab Section: 16
# Sources, people worked with, help given to:
# Jhett Carr
# lab section


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def adv_convert(num):
    negative = False
    if num[0] == "-":
        negative = True
        num = num.replace("-", "")

    if "." in num:
        numsplit = num.split(".") # [somenumber, somenumber]
        if len(numsplit) == 2 and numsplit[0].isdigit() and numsplit[1].isdigit():
            if negative:
                return -1*float(num)
            else:
                return float(num)
        else:
            return False

    elif num.isdigit():
        if negative:
            return -1*int(num)
        else:
            return int(num)
    return False:



print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, x_lower, x_upper):
    """Calculate y = mx + b for all integer x values from x_lower to x_upper."""
    # Ensure bounds are integers and lower bound is less than or equal to upper bound
    if not (isinstance(x_lower, int) and isinstance(x_upper, int)):
        return False
    if x_lower > x_upper:
        return False
    
    # Calculate y values for each x in the range [x_lower, x_upper]
    y_values = [(m * x + b) for x in range(x_lower, x_upper + 1)]
    return y_values

def main():
    while True:
        # Get user input
        user_input = input("Enter m, b, x_lower, x_upper (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        
        try:
            # Parse input values
            m, b, x_lower, x_upper = map(float, user_input.split())
            x_lower, x_upper = int(x_lower), int(x_upper)  # Ensure bounds are integers
        except ValueError:
            print("Invalid input. Please enter four numbers.")
            continue

        # Call the function and print the results
        result = slope_intercept(m, b, x_lower, x_upper)
        
        if result is False:
            print("Invalid bounds. Ensure bounds are integers and lower <= upper.")
        else:
            print(f"y values for x from {x_lower} to {x_upper}: {result}")

if __name__ == "__main__":
    main()

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

import math

def safe_sqrt(value):
    """Return the square root of a number if non-negative, else None."""
    if value < 0:
        return None
    return math.sqrt(value)

def solve_quadratic(a, b, c):
    """Solve the quadratic equation ax^2 + bx + c = 0."""
    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c
    sqrt_discriminant = safe_sqrt(discriminant)
    
    if sqrt_discriminant is None:
        return None, None  # No real roots
    
    # Calculate the two solutions
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    return root1, root2

def main():
    while True:
        try:
            # Get user input
            a = float(input("Enter value for a (non-zero): "))
            if a == 0:
                print("Coefficient 'a' cannot be zero. Please try again.")
                continue
            b = float(input("Enter value for b: "))
            c = float(input("Enter value for c: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        # Solve the quadratic equation
        root1, root2 = solve_quadratic(a, b, c)
        
        if root1 is None and root2 is None:
            print("No real roots.")
        else:
            print(f"The roots of the equation are: {root1} and {root2}")
        
        # Prompt user to continue or exit
        cont = input("Would you like to solve another equation? (yes/no): ").strip().lower()
        if cont != "yes":
            break

if __name__ == "__main__":
    main()

