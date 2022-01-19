import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Graph:
    def initialize(self):
        style.use('fivethirtyeight')
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1,1,1)
        self.x = 0
        self.points = []

    def animate(self, i):
        xs = []
        ys = []

        for point in self.points:
            xs.append(point.getX())
            ys.append(point.getY())

        self.ax1.clear()
        self.ax1.plot(xs, ys)

    def show(self):
        ani = animation.FuncAnimation(self.fig, self.animate, interval=1000)
        plt.show()

    def addValue(self, value):
        if len(self.points) >= 15:
            self.points.pop(0)

        self.points.append(Point(self.x, value))
        self.x += 1

