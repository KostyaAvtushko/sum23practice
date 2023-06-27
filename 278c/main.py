import matplotlib.pyplot as plt
import numpy as np

plt.axhline(0)
plt.axvline(0)

x3 = np.arange(-10, 10, 0.01)
plt.plot(x3, 2**x3)

plt.show()



