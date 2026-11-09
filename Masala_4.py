import matplotlib.pyplot as plt

tillar = ["Python", "C", "JavaScript", "Java"]
oquvchilar = [15, 8, 12, 5]

plt.pie(oquvchilar,labels=tillar,autopct="%1.2f%%")

plt.show()