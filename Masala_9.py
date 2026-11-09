import matplotlib.pyplot as plt

kunlar = ["Du", "Se", "Cho", "Pa", "Ju", "Sha", "Ya"]
sotilgan = [3,5,4,8,10,2,15]

plt.plot(kunlar,sotilgan,color="black",marker="o",linestyle="-.")
plt.title("Sotilgan Moshinalar")
plt.ylabel("Sotilganlar soni")
plt.xlabel("Hafta kunlari")
plt.grid(True)

plt.savefig("natija.png")
plt.show()