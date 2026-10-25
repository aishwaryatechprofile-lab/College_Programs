import matplotlib.pyplot as plt

month = ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]

rainfall = [15, 20, 35, 60, 120, 250, 300, 280, 200, 100, 40, 20]

plt.plot(month, rainfall, marker='o')

plt.title("Monthly Rainfall of a City")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")

plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()