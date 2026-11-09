from matplotlib import pyplot as plt

kunlar = [1, 2, 3, 4, 5, 6, 7]
harorat = [18, 20, 17, 23, 25, 22, 27]

plt.plot(kunlar,harorat,marker="o")

plt.title("7 KUNLIK OB-HAVO")
plt.xlabel("Kunlar")
plt.ylabel("Haroratlar")

plt.grid(True)

plt.show()