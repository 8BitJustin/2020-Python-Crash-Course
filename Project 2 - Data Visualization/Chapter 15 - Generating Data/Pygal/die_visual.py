import pygal
from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = [die.roll() for roll_num in range(1000)]
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

# Analyze results.
frequencies = []
for value in range(1, die.roll()+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
# x_labels altered to list comprehension per 15.6.
hist.x_labels = list(range(1, 7))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file('die_visual.svg')