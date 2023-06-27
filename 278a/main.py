import matplotlib.pyplot as plt
import numpy as np

plt.axhline(0)
plt.axvline(0)

x1 = np.arange(-10, 10, 0.01)
plt.plot(x1, (1/2)**x1)

plt.show()