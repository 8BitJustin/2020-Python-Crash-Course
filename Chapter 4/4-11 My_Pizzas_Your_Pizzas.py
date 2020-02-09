pizzas = ["pepperoni", "sausage", "black olive", "ham"]
friends_pizza = pizzas[:]

pizzas.append("bacon")
friends_pizza.append("pineapple")

print("My favorite pizzas are:")
for j in pizzas:
    print("\t" + j.title())

print("My friends favorite pizzas are:")
for j in friends_pizza:
    print("\t" + j.title())
