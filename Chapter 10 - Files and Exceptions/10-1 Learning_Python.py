# Reads entire file.

with open('learning_python.txt') as file_object_01:
    contents = file_object_01.read()
    print(contents)


# Reads by looping over file object.

file = 'learning_python.txt'

with open(file) as file_object_02:
    lines = file_object_02.readlines()

for line in lines:
    print(line.rstrip())


# Storing in a list, printing outside of with block

py_string = ''

for line in lines:
    py_string += line.rstrip()

print(py_string)