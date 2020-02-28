prompt = "Want to see if a number is a multiple of 10?"
prompt += "\nPlease give a number: "

number = input(prompt)
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of ten!")
else:
    print(str(number) + " is not a multiple of ten.")