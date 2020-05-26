"""学习numpy array的生成方法"""
import matplotlib.pyplot as plt

import numpy as np

x = np.arange(9)

y = np.sin(x)

z = np.cos(x)

plt.plot(x, y, marker="*", linewidth=3, linestyle="--", color="orange")

plt.plot(x, z)

plt.title("Python matplotlib Demo - By hanshiqiang365")

plt.xlabel("width")

plt.ylabel("height")

plt.legend(["Y","Z"], loc="upper right")

plt.grid(True)

plt.show()
