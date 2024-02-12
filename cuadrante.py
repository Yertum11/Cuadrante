def determine_quadrant(x, y):
    """
    Determines the quadrant in which a point is located based on its coordinates (x, y).

    Parameters:
    - x (int): The x-coordinate of the point.
    - y (int): The y-coordinate of the point.

    Returns:
    str: A message indicating the quadrant in which the point is located.
    """
    if x > 0 and y > 0:
        return "The point is located in the first quadrant."
    elif x < 0 and y > 0:
        return "The point is located in the second quadrant."
    elif x < 0 and y < 0:
        return "The point is located in the third quadrant."
    elif x > 0 and y < 0:
        return "The point is located in the fourth quadrant."
    elif x == 0 and y != 0:
        return "The point is located on the Y-axis."
    elif x != 0 and y == 0:
        return "The point is located on the X-axis."
    elif x == 0 and y == 0:
        return "The point is located at the origin."


# Ask the user to input coordinates
try:
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))

    # Determine the quadrant
    result = determine_quadrant(x, y)

    # Print the result
    print(result)

except ValueError:
    print("Error: Enter valid integer values for x and y.")
