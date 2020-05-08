import matplotlib.pyplot as plt
from die import Die

die_1 = Die()

results = [die_1.roll() for roll in range(100)]
plt.figure(figsize=(12, 4))
plt.title("6-sided rolls")
plt.xlabel("Roll")
plt.ylabel("Side")

plt.plot(results, linewidth=4)

plt.show()