from basic_shapes import Circle, Rectangle, Square
from advanced_shapes import Sphere, Cuboid

def main():
    print("Choose a shape to work with:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Sphere")
    print("5. Cuboid")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        radius_circle = float(input("Enter the radius of the circle: "))
        circle = Circle(radius_circle)
        print("Circle - Area:", circle.area())
        print("Circle - Perimeter:", circle.perimeter())
    elif choice == 2:
        length_rectangle = float(input("Enter the length of the rectangle: "))
        width_rectangle = float(input("Enter the width of the rectangle: "))
        rectangle = Rectangle(length_rectangle, width_rectangle)
        print("Rectangle - Area:", rectangle.area())
        print("Rectangle - Perimeter:", rectangle.perimeter())
    elif choice == 3:
        side_square = float(input("Enter the side length of the square: "))
        square = Square(side_square)
        print("Square - Area:", square.area())
        print("Square - Perimeter:", square.perimeter())
    elif choice == 4:
        radius_sphere = float(input("Enter the radius of the sphere: "))
        sphere = Sphere(radius_sphere)
        print("Sphere - Volume:", sphere.volume())
    elif choice == 5:
        length_cuboid = float(input("Enter the length of the cuboid: "))
        width_cuboid = float(input("Enter the width of the cuboid: "))
        height_cuboid = float(input("Enter the height of the cuboid: "))
        cuboid = Cuboid(length_cuboid, width_cuboid, height_cuboid)
        print("Cuboid - Volume:", cuboid.volume())
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
