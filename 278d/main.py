import matplotlib.pyplot as plt
import numpy as np
from math import e

plt.axhline(0)
plt.axvline(0)

x4 = np.arange(-10, 10, 0.01)
plt.plot(x4, e**x4)

plt.show()
