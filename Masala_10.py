import matplotlib.pyplot as plt


ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

max_ball = max(ballar)
min_ball = min(ballar)
eng_yuqori_oquvchi = ismlar[ballar.index(max_ball)]
eng_past_oquvchi = ismlar[ballar.index(min_ball)]
ortacha_ball = sum(ballar) / len(ballar)

print(f"Eng yuqori ball: {eng_yuqori_oquvchi} ({max_ball})")
print(f"Eng past ball: {eng_past_oquvchi} ({min_ball})")
print(f"O'rtacha ball: {ortacha_ball:.2f}")


a = plt.bar(ismlar, ballar, color="red",width=0.5)
plt.bar_label(a)

plt.title("O'quvchilarning test natijalari")
plt.xlabel("O'quvchilar ismlari")
plt.ylabel("Ball")
plt.grid(True,linestyle="--")

plt.savefig("oquvchilar_natijasi.png")

plt.show()