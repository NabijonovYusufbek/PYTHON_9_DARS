import matplotlib.pyplot as plt

mahsulotlar = ["Non", "Sut", "Tuxum", "Yog", "Shakar"]
sotuv = [45, 30, 60, 20, 25]

a = plt.bar(mahsulotlar,sotuv,width=0.5,color="blue")

plt.bar_label(a)
plt.title("Sotilgan mahsulotlar soni")
plt.ylabel("Sotilganlar soni")

plt.show()