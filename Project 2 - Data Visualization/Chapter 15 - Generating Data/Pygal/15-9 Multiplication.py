import pygal
from die import Die

die_1 = Die()
die_2 = Die()

results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]
max_result = die_1.sides * die_2.sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = list(range(1, 37))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 * D6", frequencies)
hist.render_to_file('multiplication.svg')