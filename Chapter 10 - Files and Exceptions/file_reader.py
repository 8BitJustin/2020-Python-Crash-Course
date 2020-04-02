# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)
#     print(contents.rstrip())


filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        # rstrip removes blank spaces after last line finishes
        print(line.rstrip())