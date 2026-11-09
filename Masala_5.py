import matplotlib.pyplot as plt

mashgulot = [1, 2, 3, 4, 5, 6]
masofa = [2.0, 2.5, 2.3, 3.0, 3.5, 4.0]

plt.plot(mashgulot,masofa,marker="p",color="yellow",linewidth=2.5)
plt.grid(True,linestyle="--")
plt.xlabel("Kunlar")
plt.ylabel("Masofa")

plt.show()