import random as r
import matplotlib.pyplot as plt

class RandomWalk:
    """A class for random walks"""

    def __init__(self, ps=5000):
        self.num_points = ps
        self.xs = [0]
        self.ys = [0]

    def fill_walk(self):
        while len(self.xs) < self.num_points:
            dirs = [1, -1]
            dists = [0, 1, 2, 3, 4]

            x_dir = r.choice(dirs)
            x_dist = r.choice(dists)
            x_step = x_dist * x_dir

            y_dir = r.choice(dirs)
            y_dist = r.choice(dists)
            y_step = y_dist * y_dir

            if x_step == 0 and y_step == 0:
                continue

            x = self.xs[-1] + x_step
            y = self.ys[-1] + y_step

            self.xs.append(x)
            self.ys.append(y)

while True:
    rw = RandomWalk(ps=100_000)
    rw.fill_walk()
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15.6, 9.2))
    point_nums = range(rw.num_points)
    ax.scatter(rw.xs, rw.ys, c=point_nums, cmap=plt.cm.Blues, s=1, edgecolors='none')
    ax.scatter(0, 0, c="green", edgecolors="none", s=50)
    ax.scatter(rw.xs[-1], rw.ys[-1], c="red", edgecolors="none", s=50)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    run = input("another one (\"no\" to quit): ")
    if run == "no":
        break
