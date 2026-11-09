import matplotlib.pyplot as plt

testlar = [1, 2, 3, 4, 5]
guruh_a = [65, 70, 75, 80, 85]
guruh_b = [60, 72, 70, 88, 90]

plt.plot(testlar,guruh_a,color="red",marker="o",label="A_guruh")
plt.plot(testlar,guruh_b,color="yellow",marker="p",label="B_guruh")

plt.legend()
plt.title("Test natijalari")
plt.xlabel("Testlar")
plt.ylabel("Ballar")
plt.grid(True)

plt.show()