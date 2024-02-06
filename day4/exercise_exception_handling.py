try:
    # Read data from file
    with open('cal_values.txt', 'r') as file:
        data = file.readlines()

    # Process the data
    for line in data:
        # Split the line by whitespace and convert values to integers
        values = [int(val) for val in line.split()]
        
        # Perform processing tasks using the values
        if len(values) >= 2:  # Ensure there are at least two values
            a, b = values[:2]  # Extract the first two values
            print("Values read from file:", a, b)
            
            # Example processing tasks
            add = a + b
            print("Addition:", add)
            
            sub = a - b
            print("Subtraction:", sub)
            
            mul = a * b
            print("Multiplication:", mul)
            
            # Attempt division operation
            try:
                div = a / b
                print("Division:", div)
            except ZeroDivisionError:
                print("Error: Division by zero.")
                
        else:
            print("Insufficient values in the line:", line.strip())

except FileNotFoundError:
    print("Error: File not found.")
except ValueError:
    print("Error: Unable to convert data to integers.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
finally:
    # Clean-up code, if necessary
    pass
