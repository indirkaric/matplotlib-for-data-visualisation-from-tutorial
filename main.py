from turtle import color
from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([0, 6])
y_points = np.array([0, 250])

# display simple plot
plt.plot(x_points, y_points)
plt.show()

x_points = np.array([1, 8])
y_points = np.array([3, 10])

plt.plot(x_points, y_points, 'o')  #no line plot
plt.show()

# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
x_points = np.array([1, 2, 6, 8])
y_points = np.array([3, 8, 1, 10])

plt.plot(x_points, y_points)
plt.show()

# plotting without x points
y_points = np.array([3, 8, 1, 10, 5, 7])

plt.plot(y_points)
plt.show()

# working with markers

x_points = np.array([1, 2, 6, 8])
y_points = np.array([3, 8, 1, 10])

# to set size of marker use field ms  example ms = 20
# for marker edge color use mc field example mc = 'r'
# we can use hexadecimal colors
plt.plot(x_points, y_points, marker = '*')
plt.show()

# working with lines

x_points = np.array([1, 2, 6, 8])
y_points = np.array([3, 8, 1, 10])

#  set label and title 
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x_points, y_points, marker = '*', color = 'r', linestyle = 'dashed', linewidth = '5.5')
plt.show()

# working with the grid system

plt.plot(x_points, y_points, marker = '*', color = 'r', linestyle = 'dashed', linewidth = '2.5')
# we can have grid for one axis plt.grid(axis = 'y')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()


# workign with subplots
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

# one row 2 columns and this is first plot
plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("INCOME")
plt.show()

# working with bars

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1, color = 'r')
plt.show()

# pie chart

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 