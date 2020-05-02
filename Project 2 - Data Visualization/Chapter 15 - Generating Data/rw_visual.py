import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making random walks as long as program is active.
while True:
    # Make random walk, and plot points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    fig = plt.figure(figsize=(15, 8))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red",
                edgecolors="none", s=100)

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
