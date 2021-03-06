from die import Die
import pygal

# Create D6 and D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, store results in a list.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze results.
frequencies = []
max_result = die_1.sides + die_2.sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize results.
hist = pygal.Bar()

hist.title = "Results of rolling a D6 die and a D10 die 50000 times."
# x_labels altered to list comprehension per 15.6.
hist.x_labels = list(range(2, 17))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D10", frequencies)
hist.render_to_file('different_dice_visual.svg')
