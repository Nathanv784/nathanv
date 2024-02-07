# List of numbers
numbers = [1, 2, 3, 4, 5]

# List comprehension to create a list of squares of numbers
squares = [x**2 for x in numbers]

# List comprehension to filter even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

# List comprehension to create a list of tuples containing the number and its square
number_square_pairs = [(x, x**2) for x in numbers]

# List comprehension to create a list of uppercase strings
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]

# Print results
print("List of numbers:", numbers)
print("Squares of numbers:", squares)
print("Even numbers:", even_numbers)
print("Number-square pairs:", number_square_pairs)
print("Uppercase words:", uppercase_words)
