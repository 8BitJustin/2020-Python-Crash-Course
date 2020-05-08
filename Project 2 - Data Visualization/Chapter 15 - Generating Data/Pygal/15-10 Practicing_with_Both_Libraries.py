import matplotlib.pyplot as plt
from die import Die

die_1 = Die()

results = [die_1.roll for roll in range(100)]

x_values = list(range(1, 7))
y_values = results

plt.scatter(x_values, y_values, s=100)

plt.title("6-sided rolls")
plt.xlabel("Side")
plt.ylabel("Results")

plt.show()
