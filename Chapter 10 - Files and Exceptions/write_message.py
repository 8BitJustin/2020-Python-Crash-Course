filename = 'programming.txt'

with open(filename, 'w') as file_object:
    # Creates programming.txt file, writes first line, goes to new line,
    # writes following line.
    file_object.write('I love programming!\n')
    file_object.write('I love creating programs.\n')


with open(filename, 'a') as file_object:
    # This 'appends' text to the programming.txt file.
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')