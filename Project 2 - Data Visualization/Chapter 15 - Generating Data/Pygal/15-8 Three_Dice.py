import pygal
from die import Die

# OMG 3 DIE?!?!
die_1 = Die()
die_2 = Die()
die_3 = Die()

results = [die_1.roll() + die_2.roll() + die_3.roll() for roll in range(1000)]
max_result = die_1.sides + die_2.sides + die_3.sides

frequencies = [results.count(value) for value in range(3, max_result+1)]

hist = pygal.Bar()
hist.title = "Results of rolling...OMG...THREE D6 die!!!"
hist.x_labels = list(range(3, 19))
hist.x_title = "Results"
hist.y_labels = "Frequency of Results"

hist.add("D6 X 3!!!")
hist.render_to_file('three_die_visual.svg')
