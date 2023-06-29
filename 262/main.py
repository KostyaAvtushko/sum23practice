import matplotlib.pyplot as plt
import numpy as np

plt.axhline(0)
plt.axvline(0)

x = np.arange(-10, 10, 0.01)
plt.ylim(-3,3)
plt.plot(x,((x + 1)*(x - 2))/((x - 1)*(x + 2)))

plt.show()
