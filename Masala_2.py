import matplotlib.pyplot as plt

fanlar = ["Matematika", "Python", "Ingliz tili", "Fizika", "Tarix"]
ballar = [85, 95, 72, 80, 88]

a = plt.bar(fanlar,ballar)

plt.bar_label(a)
plt.title("O'quvchining ballari")
plt.ylabel("Ballar")


plt.show()