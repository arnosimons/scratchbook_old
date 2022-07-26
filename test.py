mysum = 4 + 3
import matplotlib.pyplot as plt
class Session:
  def __init__(self, numbers):
    self.fig = plt.gcf()
    self.ax = plt.gca()
    self.ax.plot(numbers)
