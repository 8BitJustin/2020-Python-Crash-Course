import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 9, 27, 81, 243]
plt.plot(x, y, linewidth=3)

plt.title('Cubed', fontsize=24)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Qubed Value", fontsize=12)

plt.tick_params(axis='both', labelsize=14)

plt.show()