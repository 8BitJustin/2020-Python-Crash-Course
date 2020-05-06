import pygal
from die import Die

die_1 = Die(8)
die_2 = Die(8)

results = [die_1.roll() + die_2.roll() for roll in range(1000000)]
max_result = die_1.sides + die_2.sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

hist = pygal.Bar()
hist.x_labels = list(range(2, 17))
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add("D8 + D8", frequencies)
hist.render_to_file('d8_15_7.svg')