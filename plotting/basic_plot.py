import random
from matplotlib import pyplot

x_values= [0, 4, 7, 20, 22, 25]
y_values= [random.randint(0, 200)for elt in x_values]
pyplot.plot(x_values, y_values, "o-")

pyplot.ylabel("Value")
pyplot.xlabel("Time")
pyplot.title("Test plot")

pyplot.show()
