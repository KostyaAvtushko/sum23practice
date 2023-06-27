import matplotlib.pyplot as plt
import numpy as np

plt.axhline(0)
plt.axvline(0)

x1 = np.arange(-10, 0, 0.01)

plt.plot(x1, (-x1 - 2)**0.5, x1, -((-x1 - 2)**0.5))


plt.show()

