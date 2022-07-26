mysum = 4 + 3
import matplotlib.pyplot as plt
def session(numbers):
  fig = plt.gcf()
  ax = plt.gca()
  ax.plot(numbers)
  return fig
