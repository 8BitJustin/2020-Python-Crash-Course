from die import Die

# Create D6.
die = Die()

# Make some rolls, store results in a list.
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze results.
frequencies = []
for value in range(1, die.sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)