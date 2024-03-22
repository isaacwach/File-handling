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