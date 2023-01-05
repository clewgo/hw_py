from random import randint as rnd

# 1.

k = 1
x = 0
for k in range(1, 1000000):
    x = x + 4 * ((-1)**(k + 1)) / (2 * k - 1)

print(round(x, int(input("Задайте число знаков числа pi после запятой: "))))

print("---------------------------------")

# 2.

n = int(input("Задайте натуральное число: "))
list_x = []
divider = 2
while divider * divider <= n:
    if n % divider == 0:
        list_x.append(divider)
        n //= divider
    else:
        divider += 1
if n > 1:
    list_x.append(n)

print(f"Простые множители: {list_x}")

print("---------------------------------")

# 3.

print(*set(map(int, input("Введите числа через пробел: ").split(" "))))

print("---------------------------------")

# 4.

degree = int(input("Введите наивысшую степень: "))
list_x = list()
str_x = str()
for i in range(degree, -1, -1):
    multiplier = rnd(0,100)
    if multiplier != 0:
        if multiplier == 1:
            temp = ""
        else:
            temp = str(multiplier)
        if i not in [0,1]:
            list_x += [f"{temp}X^{i}"]
        elif i == 1:
            list_x += [f"{temp}X"]
        else:
            list_x += [f"{temp}"]
for i in range(len(list_x)):
    if i != len(list_x) -1:
        str_x += f"{list_x[i]} + "
    else:
        str_x += f"{list_x[i]} = 0"

with open("file.txt", "w") as out:
    out.writelines(str_x)

print("---------------------------------")