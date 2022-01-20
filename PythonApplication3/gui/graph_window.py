import oid
import threading
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

class GraphWindow:
    def __init__(self, sshConnection, snmpConnection):
        self.sshConnection = sshConnection
        self.snmpConnection = snmpConnection
        self.figure = plt.figure()
        self.graphPlotter = self.figure.add_subplot(1,1,1)
        self.offsetReqValue = snmpConnection.get([oid.IP_REQUEST])
        self.reqValue = 0
        self.x = 0
        self.xs = []
        self.ys = []

    def animate(self, i):
        self.graphPlotter.clear()
        self.graphPlotter.plot(self.xs, self.ys)

    def show(self):
        self.updateThread = threading.Thread(target=self.updateThread)
        self.updateThread.start();

        style.use('fivethirtyeight')
        ani = animation.FuncAnimation(self.figure, self.animate, interval=1000)
        plt.show()

    def updateThread(self):
        while 1:
            if len(self.xs) >= 100:
                self.xs.pop(0)
                self.ys.pop(0)

            self.offsetReqValue += 1;
            self.reqValue = self.snmpConnection.get([oid.IP_REQUEST]) - self.offsetReqValue
            self.xs.append(self.x)
            self.ys.append(self.reqValue)
            self.x += 1
            time.sleep(1)
