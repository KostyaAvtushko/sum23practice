import matplotlib.pyplot as plt
import numpy as np

plt.axhline(0)
plt.axvline(0)

x1 = np.arange(-10, 0, 0.01)
x2 = np.arange(0, 10, 0.01)
plt.plot(x1, x1 + 1/x1, x2, x2 + 1/x2)


plt.show()


