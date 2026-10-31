import subplot_example.pyplot as plt

plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [10, 20, 30])
plt.title("Line Graph")

plt.subplot(1, 2, 2)
plt.bar(["A", "B"], [10, 20])
plt.title("Bar Graph")

plt.show()