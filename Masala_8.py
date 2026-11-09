import matplotlib.pyplot as plt

soat = [1, 2, 3, 4, 5, 6, 7]
ball = [40, 48, 55, 65, 72, 85, 90]

plt.scatter(soat,ball,color = "red",s=20)
plt.xlabel("Soatlar")
plt.ylabel("Ballar")
plt.grid(True)

plt.show()