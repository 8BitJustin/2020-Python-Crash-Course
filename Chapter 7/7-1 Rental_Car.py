prompt = "Let\'s see if you are old enough to rent a car."
prompt += "\nHow old are you? "

age = input(prompt)
age = int(age)

if age >= 18:
    print("You can rent a car!")
else:
    print("You can not rent a car.")