import sys
import matplotlib.pyplot as plt

print(f"Version {matplotlib.__version__} installed")
if matplotlib.__version__[0] == "0":
    sys.exit("Version incorrectly starts with 0")

x = [2, 4, 5]
y = [2, 3, 6]

plt.plot(x, y)

plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph ')

plt.show()