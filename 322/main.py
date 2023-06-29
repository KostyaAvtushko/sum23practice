import matplotlib.pyplot as plt
import numpy as np

plt.axhline(0)
plt.axvline(0)

x1 = np.arange(-10, 10, 0.01)
plt.ylim(-3,3)
plt.plot(x1, np.arcsin(2*np.sin(2*x1)))

plt.show()
