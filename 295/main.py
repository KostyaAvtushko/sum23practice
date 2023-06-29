import matplotlib.pyplot as plt
import numpy as np

plt.axhline(0)
plt.axvline(0)

x1 = np.arange(-2*np.pi, 2*np.pi, 0.01)
plt.ylim(-3,3)
plt.plot(x1, 1/np.tan(x1)**2)

plt.show()
