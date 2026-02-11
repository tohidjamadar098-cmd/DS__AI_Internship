# Define the function
def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter  # Returning multiple values as a tuple

# Get user input
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Call the function
area, perimeter = calc_rectangle(length, width)

# Print the result
print(f"Area: {area}, Perimeter: {perimeter}")
