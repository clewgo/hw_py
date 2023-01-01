# 1.

a = int(input("Введите число монеток: "))
b = 0
for r in range(a):
    i = int(input(f"Введите {r + 1} монетку: "))
    if i == 1:
        b += 1
print(f"Минимальное количество монет, которые нужно перевернуть = {b if b < a / 2 else a - b}")

print("---------------------------------")

# 2.

a = int(input("Введите число: "))
b = 0
if a > 0:
    for i in range(1, a + 1):
        b += i
elif a < 0:
    for i in range(1, a - 1, -1):
        b += i
elif a == 0:
    b = 1
print(f"Cумма целых чисел, расположенных между 1 и {a} включительно = {b} ")

print("---------------------------------")

# 3.

a = int(input("Введите число: "))
b = 1
while b <= a:
    b = b + 1
    if a % b == 0:
        print(f"Наименьший натуральный делитель числа {a} = {b}")
        break

print("---------------------------------")

# 4.

n = int(input("Введите количество учеников: "))
h = []
for i in range(n):
    heigth = int(input(f"Рост {i + 1} ученика: "))
    h.append(heigth)
petya = int(input("Рост Пети: "))
h.append(petya)
h.sort(reverse=True)
print(f"Номер Пети в шеренге учеников = {h.index(petya) + 1}")