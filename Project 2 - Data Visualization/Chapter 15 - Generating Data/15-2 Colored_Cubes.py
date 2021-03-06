import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolors='none', s=20)

plt.title('Cubed', fontsize=24)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Cubed Value", fontsize=12)

plt.tick_params(axis='both', labelsize=14)

plt.show()