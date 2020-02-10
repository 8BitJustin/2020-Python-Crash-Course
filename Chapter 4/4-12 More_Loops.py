my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are:")
for j in my_foods:
    print("\t" + j.title())

print("My friends favorite foods are:")
for j in friend_foods:
    print("\t" + j.title())