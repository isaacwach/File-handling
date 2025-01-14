# File creation
with open("my_file.txt", "w") as file:
    file.write("Welcome to file handling module\n")
    file.write("This is module 6\n")
    file.write("30\n")
    file.write("Successfuly finishing the module will require absolute dedication, worjing for more than 10 hours a day.\n")

# File reading and display
with open("my_file.txt", "r") as file:
    content = file.read()
    print("The file contents are:\n")
    print(content)

# File appending
with open("my_file.txt", "a") as file:
    file.write("Hello, hope you enjoye the module\n")
    file.write("See you next week\n")
    file.write("remember to complete the assignment\n")

# Error Handling
try:
    with open("non_existent_file.txt", "r") as file:
        contents = file.read()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("Thank ypu for checking our course")