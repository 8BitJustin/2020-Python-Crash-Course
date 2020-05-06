import pygal
from die import Die

# Create a two D6.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
# results variable/list altered to list comprehension per 15.6.
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# Analyze results.
frequencies = []
max_result = die_1.sides + die_2.sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
# x_labels altered to list comprehension per 15.6.
hist.x_labels = list(range(2, 13))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D6", frequencies)
hist.render_to_file('dice_visual.svg')