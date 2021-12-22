import matplotlib.pyplot as plt

plt.style.use("seaborn")

vals = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, (ax1, ax2) = plt.subplots(1, 2)

fig.set_figwidth(12.8)

ax1.plot(vals, squares, linewidth=3)

ax1.set_title("Square Numbers", fontsize=24)
ax1.set_xlabel("Value", fontsize=14)
ax1.set_ylabel("Square of Value", fontsize=14)

ax1.tick_params(axis="both", labelsize=14)

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

ax2.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax2.set_title("Square Numbers", fontsize=24)
ax2.set_xlabel("Value", fontsize=14)
ax2.set_ylabel("Square of Value", fontsize=14)

ax2.tick_params(axis="both", labelsize=14)

ax2.axis([0, 1100, 0, 1100000])

plt.show()
