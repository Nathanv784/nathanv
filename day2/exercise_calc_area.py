l1=[76, 23, 45, 12, 54, 9]
print("Original List:", l1)
 
# sorting list using nested loops
for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j],l1[i]
 
# sorted list
print("Sorted List", l1)
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

def square_area(side_length):
    """
    Calculate the area of a square given the length of its side.
    """
    return side_length ** 2

def triangle_area(base, height):
    """
    Calculate the area of a triangle given its base and height.
    """
    return 0.5 * base * height

# Example usage:
square = Shape("Square")
triangle = Shape("Triangle")

# Set side length for square
side_length = 5

# Set base and height for triangle
base = 5
height = 3

# Calculate area for square and triangle
square_area_value = square_area(side_length)
triangle_area_value = triangle_area(base, height)

print(f"Area of the {square.name} with side length {side_length} is: {square_area_value}")
print(f"Area of the {triangle.name} with base {base} and height {height} is: {triangle_area_value}")
