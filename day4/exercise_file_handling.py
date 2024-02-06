file_path = "example.txt"

# Writing and reading with 'w' mode
with open(file_path, "w") as file:
    file.write("using write mode\n")

# Reading with 'r' mode
with open(file_path, "r") as file:
    content = file.read()
    print("Content in 'r' mode:", content)

# Appending with 'a' mode
with open(file_path, "a") as file:
    file.write("using append mode\n")

# Reading and writing with 'r+' mode
with open(file_path, "r+") as file:
    file.seek(0)
    print("Content in 'r+' mode before writing:", file.read())
    file.write("New content\n")
    file.seek(0)
    print("Content in 'r+' mode after writing:", file.read())

# Reading and appending with 'a+' mode
with open(file_path, "a+") as file:
    file.seek(0)
    print("Content in 'a+' mode before appending:", file.read())
    file.write("Another line\n")
    file.seek(0)
    print("Content in 'a+' mode after appending:", file.read())

# Demonstrating the use of tell() function
with open(file_path, "r") as file:
    file.seek(0, 2)
    print("Current position in file:", file.tell())
