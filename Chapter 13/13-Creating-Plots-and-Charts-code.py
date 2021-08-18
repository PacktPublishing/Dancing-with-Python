import inspect

import matplotlib.pyplot as plt

the_plot = plt.plot(1, 0.5, color="black", marker='o')

import matplotlib.pyplot as plt

plt.clf()                   # clear the previous figure

plt.grid()                  # include a background grid

plt.axhline(color="black")  # draw a horizontal axis in black
plt.xlabel('x')             # label the horizontal axis as 'x'

plt.axvline(color="black")  # draw a vertical axis in black
plt.ylabel('y')             # label the vertical axis as 'y'

plt.title("Plot with grid, axes, and title")  # set the title

the_plot = plt.plot(1, 0.5, color="black", marker='o')

from mpl_helper_1 import initialize_plot

print(inspect.getsource(initialize_plot))

import matplotlib.pyplot as plt
from mpl_helper_1 import initialize_plot

figure, axes = initialize_plot('x', 'y',
    "Setting the aspect ratio for the axes")

# --------------------------------------------------------------
# set the aspect ratio of vertical to horizontal
axes.set_aspect('equal')
# --------------------------------------------------------------

the_plot = axes.plot(1, 0.5, color="black", marker='o')

import matplotlib.pyplot as plt
from mpl_helper_1 import initialize_plot

figure, axes = initialize_plot('x', 'y')

# set the aspect ratio of vertical to horizontal
axes.set_aspect('equal')

# --------------------------------------------------------------
for position in ("top", "right", "bottom", "left"):
    # turn off the extra lines around the plot
    axes.spines[position].set_visible(False)

axes.set_title("Plot with annoying\nouter lines removed",
               fontsize=20, fontstyle="italic")
# --------------------------------------------------------------

the_plot = axes.plot(1, 0.5, color="black", marker='o')

from mpl_helper_2 import initialize_plot

print(inspect.getsource(initialize_plot))

import matplotlib.pyplot as plt
from mpl_helper_2 import initialize_plot

figure, axes = initialize_plot('x', 'y',
    "Plot with an extra point added")

# set the aspect ratio of vertical to horizontal
axes.set_aspect('equal')

axes.plot(1.0,  0.5,  color="black", marker='o')
axes.plot(0.25, 0.25, color="black", marker='o')

import matplotlib.pyplot as plt
from mpl_helper_2 import initialize_plot

figure, axes = initialize_plot('x', 'y',
    "Plot with a line between two points")

# set the aspect ratio of vertical to horizontal
axes.set_aspect('equal')

# --------------------------------------------------------------
x_values = [1.0, 0.25]
y_values = [0.5, 0.25]
# --------------------------------------------------------------

the_plot = axes.plot(x_values, y_values, color="black", marker='o')

import matplotlib.pyplot as plt
from mpl_helper_2 import initialize_plot

figure, axes = initialize_plot('x', 'y',
    "Plot with two lines and a labeled point")

# set the aspect ratio of vertical to horizontal
axes.set_aspect('equal')

x_values = [1.0, 0.25]
y_values = [0.5, 0.25]
axes.plot(x_values, y_values, color="black", marker='o')

# draw a point with a square shape
axes.plot(0.5, 0.4, marker='s')

# label the point with the text centered
axes.text(0.5, 0.43, "(0.5, 0.4)", horizontalalignment="center")

# draw another line
the_plot = axes.plot([0.1, 0.3], [0.4, 0.1])

import matplotlib.pyplot as plt
from mpl_helper_2 import initialize_plot

figure, axes = initialize_plot('x', 'y',
    r"Plot of the parabola $\mathregular{y=x^2-3}$")

# --------------------------------------------------------------
x_values = list(range(-4, 5))
y_values = [x**2 - 3 for x in x_values]
# --------------------------------------------------------------

the_plot = axes.plot(x_values, y_values)

from sys import getsizeof

getsizeof("")

a = "Better a witty fool, than a foolish wit."
len(a)

getsizeof(a)

b = 100 * a
len(b)

getsizeof(b)

getsizeof([a, b])

getsizeof([b, b])

getsizeof([b, b, b])

def getsizeof_list(the_list):
    size = getsizeof(list)
    for item in the_list:
        size += getsizeof(item)
    return size

x_values = list(range(1000))
getsizeof_list(x_values)

import numpy as np

x_values_array = np.arange(1000)

getsizeof(x_values_array)

x_values_array.size

x_values_array.itemsize

x_values_array.nbytes

np.array([2, 3.4])

np.array((-1, 3.1415926j))

np.linspace(0, 1, 11)

x_values = np.linspace(-4, 4, 9)

def p(x): return x*x - 3

p(x_values)

import matplotlib.pyplot as plt
from mpl_helper_2 import initialize_plot
import numpy as np

figure, axes = initialize_plot('x', 'y',
    r"Smooth plot of the parabola $\mathregular{y=x^2-3}$")

# Generate 1000 equally spaced points between -4 and 4
x_values = np.linspace(-4, 4, 1000)

def p(x): return x*x - 3

the_plot = plt.plot(x_values, p(x_values))

import matplotlib.pyplot as plt
from mpl_helper_2 import initialize_plot
import numpy as np

figure, axes = initialize_plot('x', 'y', "y = sin(x)")

# set the aspect ratio of vertical to horizontal
axes.set_aspect('equal')

# --------------------------------------------------------------
# Generate 1000 equally spaced points between -2 pi and 2 pi
x_values = np.linspace(-2*np.pi, 2*np.pi, 1000)
# --------------------------------------------------------------

the_plot = plt.plot(x_values, np.sin(x_values))

import matplotlib.pyplot as plt
from mpl_helper_2 import initialize_plot
import numpy as np

figure, axes = initialize_plot('x', 'y', "y = sin(x)")

# set the aspect ratio of vertical to horizontal
axes.set_aspect('equal')

# --------------------------------------------------------------
# show x-coordinates from -7 to 7
axes.set_xlim([-7, 7])

# show y-coordinates from -7 to 7
axes.set_ylim([-7, 7])
# --------------------------------------------------------------

# Generate 1000 equally spaced points between -2 pi and 2 pi
x_values = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

the_plot = plt.plot(x_values, np.sin(x_values))


import matplotlib.pyplot as plt
from mpl_helper_2 import initialize_plot
import numpy as np

figure, axes = initialize_plot('x', 'y',
                               "y = sin(x)")

# set the aspect ratio of vertical to horizontal
axes.set_aspect('equal')

# show x-coordinates from -7 to 7
axes.set_xlim([-7, 7])

# show y-coordinates from -7 to 7
axes.set_ylim([-7, 7])

# --------------------------------------------------------------
# draw and label a dashed vertical line at x = -pi
axes.axvline(x=-np.pi, color="#808080",
             linestyle="dashed", linewidth=1.5)

axes.text(-4.5, -3.2,
          r"$\mathregular{x = -\pi}$",
          horizontalalignment="center")

# draw and label a dashed vertical line at x = -pi
axes.axvline(x=np.pi, color="#808080",
             linestyle="dashed", linewidth=1.5)

axes.text(4.1, -3.2,
          r"$\mathregular{x = \pi}$",
          horizontalalignment="center")
# --------------------------------------------------------------

# Generate 1000 equally spaced points between -2 pi and 2 pi
x_values = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

the_plot = axes.plot(x_values, np.sin(x_values))


import matplotlib.pyplot as plt

figure, axes = plt.subplots(1, 3)

for x in range(3):
    axes[x].set_title(f"Plot at position {x}")
    axes[x].plot(x, x, marker='o')

figure.tight_layout()

import matplotlib.pyplot as plt

figure, axes = plt.subplots(2, 3, constrained_layout=True)

for row in range(2):
    for col in range(3):
        axes[row, col].set_title(f"Plot at position {row}, {col}")
        axes[row, col].plot(row, col, marker='o')

figure.suptitle("This is a title above the figure",
                y=1.05, fontweight="bold",
                family="serif", fontsize=16)

plt.clf()

import matplotlib.pyplot as plt

data = [21, 14, 10, 9, 19]

# draw the bar chart
bar_chart = plt.bar(range(1, len(data) + 1), data)


import matplotlib.pyplot as plt

# give descriptive names to the values on the horizontal
# and vertical axes

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
support_calls = [21, 14, 10, 9, 19]

# add a title to the top of the bar chart
plt.title("Support Call Data for Last Week")

# draw the bar chart
bar_chart = plt.bar(days, support_calls)


plt.clf()

import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
support_calls = [21, 14, 10, 9, 19]

# create a list of colors for ranges of daily call values
colors = []
for calls in support_calls:
    if calls >= 15:
        colors.append("#505050")
    elif calls >= 10:
        colors.append("#808080")
    else:
        colors.append("#B0B0B0")

# add the bar chart title
plt.title("Number of Support Calls Per Day")

# draw horizontal lines
plt.grid(color="black", alpha=0.6, axis='y', linewidth=1, linestyle='--')

# draw the bar chart
bar_chart = plt.bar(days, support_calls, color=colors)


counts = {"000": 129, "001": 128, "010": 93, "011": 115,
          "100": 138, "160": 128, "113": 93, "111": 124}

plt.clf()

import matplotlib.pyplot as plt
import numpy as np

data = [[21, 14, 10, 9, 19],
        [17, 16, 4, 12, 14]]

# draw the bar chart for Team A
plt.bar(np.arange(1, len(data[0]) + 1), data[0],
        color="#505050", label="Team A")

# draw the bart chart for Team B above that of Team A
bar_chart = plt.bar(np.arange(1, len(data[1]) + 1), data[1],
                    color="#B0B0B0", label="Team B",
                    bottom=data[0])

# draw a legend identifying the bars for each team
plt.legend()


plt.clf()

import matplotlib.pyplot as plt
import numpy as np

plt.clf()

data = [[21, 14, 10, 9, 19],
        [17, 16, 4, 12, 14]]

# set the width of a bar
width = 0.4

# draw the first bar chart with each bar the specified width
bar_chart = plt.bar(np.arange(1, len(data[0]) + 1), data[0],
                    width=width, color="#505050")

# draw the second bar chart with the bars to the right of the first
bar_chart = plt.bar(np.arange(1, len(data[1]) + 1) + width, data[1],
                    width=width, color="#B0B0B0")


import matplotlib.pyplot as plt
import numpy as np

plt.clf()

np.random.seed(23)

# generate the random numbers in a normal distribution
mu = 1.0
sigma = 0.2
random_numbers = np.random.normal(mu, sigma, 1000000)

# set the number of bins in which to divide up the random numbers
bin_size = 100

# draw the histogram
the_plot = plt.hist(random_numbers, bins=bin_size)

plt.clf()

import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
support_calls = [21, 14, 10, 9, 19]

# draw the pie chart
pie_chart = plt.pie(support_calls, labels=days)

gray_shades = ["#A0A0A0", "#B0B0B0", "#C0C0C0", "#D0D0D0", "#E0E0E0"]

wedgeproperties = {'linewidth': 2, 'edgecolor': 'black'}

explode_amounts = [0.1, 0, 0, 0, 0]

plt.clf()

import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 11)

city_high_temperatures = {
    'A': np.array([63, 57, 59, 67, 54, 53, 59, 62, 62, 58]),
    'B': np.array([45, 45, 39, 31, 34, 41, 66, 63, 60, 56]),
    'C': np.array([80, 82, 82, 79, 78, 76, 76, 82, 84, 83])
}

figure, axes = plt.subplots()

# draw the scatter charts

axes.set_xlabel("Day in March, 2021")
axes.set_ylabel("Temperature in F")
axes.set_title("Daily high temperatures for three cities")

d = np.concatenate([days, days, days])
t = np.concatenate([
    city_high_temperatures['A'],
    city_high_temperatures['B'],
    city_high_temperatures['C']])

the_plot = axes.scatter(d, t)


plt.clf()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --------------------------------------------------------------
# create the plot figure
figure = plt.figure()

# create a 3D axes
axes = plt.axes(projection='3d')
# --------------------------------------------------------------

# label the x, y, and z axes in a large font
axes.set_xlabel('x', fontsize="16")
axes.set_ylabel('y', fontsize="16")
axes.set_zlabel('z', fontsize="16")

# set the limits of the values shown on the axes
axes.set_xlim(0, 1)
axes.set_ylim(0, 1)
axes.set_zlim(0, 1)

# label the origin
axes.text(0.1, 0, 0.03, "(0, 0, 0)")

# draw the axes
axes.plot([0, 0], [0, 0], [0, 1], linewidth=2, color="black")
axes.plot([0, 0], [0, 1], [0, 0], linewidth=2, color="black")
axes.plot([0, 1], [0, 0], [0, 0], linewidth=2, color="black")

# draw the point at the origin
the_plot = axes.plot([0, 0], [0, 0], [0, 0], marker='o',
                     markersize=6, color="black")


plt.clf()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# create the plot figure and 3D axes
figure = plt.figure()
axes = plt.axes(projection='3d')

# x will range from -10 to 10 for 1000 values
xs = np.linspace(-10, 10, 1000)

# y will always be 0
ys = np.full(1000, 0)

# z is the cosine of x
zs = np.cos(xs)

# draw the curve
the_plot = axes.plot(xs, ys, zs, color="black")

plt.clf()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# set the data coordinates
xs = [9, 10, 8, 4, 8, 5, 7, 2, 5, 3]
ys = [8, 1, 6, 2, 1, 3, 3, 10, 4, 3]
zs = [6, 10, 8, 1, 3, 20, 24, 26, 23, 25]

# create the plot figure and 3D axes
figure = plt.figure()
axes = plt.axes(projection='3d')

# draw the scatter plot
the_plot = axes.scatter(xs, ys, zs, color="black")


plt.clf()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# set the data coordinates
xs = np.array([0, 0, 10, 10])
ys = np.array([0, 10, 10, 0])
zs = np.array([10, 10, 10, 10])

# create the plot figure and 3D axes
figure = plt.figure()
axes = plt.axes(projection='3d')

axes.set_title("plot", fontstyle="italic")

# draw the plot for the corners
the_plot = axes.plot(xs, ys, zs, color="black")

xs = [4, 5, 6]
ys = [1, 2, 3]

x_mesh, y_mesh = np.meshgrid(xs, ys)
x_mesh

y_mesh

plt.clf()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# set the data coordinates
xs = [0, 1]
ys = [0, 1]
zs = np.array([[10, 10], [10, 10]])

# compute the grids
x_mesh, y_mesh = np.meshgrid(xs, ys)

# create the plot figure and two 3D axes
figure, axes = plt.subplots(1, 2,
                            figsize=(8, 4),
                            subplot_kw={'projection': "3d"},
                            constrained_layout=True)

# draw the wireframe plot
axes[0].set_title("plot_wireframe", fontstyle="italic")
axes[0].plot_wireframe(x_mesh, y_mesh, zs, color="black")

# draw the filled surface plot
axes[1].set_title("plot_surface", fontstyle="italic")
axes[1].plot_surface(x_mesh, y_mesh, zs, color="lightgray")

