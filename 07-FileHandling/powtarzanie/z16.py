file_name = input("Enter the name of the text file: ")

with open(file_name, 'r') as file:
    lines = file.readlines()
    number_of_lines = len(lines)
    print(f"File name: {file_name} + \n")
    print(f"Number of lines: {number_of_lines}")
