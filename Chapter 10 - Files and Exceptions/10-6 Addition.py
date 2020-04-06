print("Give two numbers, I'll multiply them.")
print("Press 'q' to quit.")

while True:
    try:
        first = input("First number: ")
        if first == 'q':
            break
        second = input("Second number: ")
        if second == 'q':
            break
        answer = int(first) * int(second)
        print(answer)
    except ValueError:
        print("Please use a number.")
