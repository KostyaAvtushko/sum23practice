import matplotlib.pyplot as plt
import numpy as np

plt.axhline(0)
plt.axvline(0)

x2 = np.arange(-10, 10, 0.01)
plt.plot(x2, 1**x2)

plt.show()


