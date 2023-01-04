# 1.

list_x = list(map(int, input("Введите числа через пробел: ").split(" ")))
sum = 0
list_y = []
print("На нечётных позициях элементы:", end=" ")

for i in range(len(list_x)):
    if i % 2 == 1:
       sum += list_x[i]
       list_y.append(list_x[i])

print(list_y)
print(f"Сумма элементов: {sum}")

print("---------------------------------")

# 2.

list_x = list(map(int, input("Введите числа через пробел: ").split(" ")))
list_y = []
for i in range(int(len(list_x) / 2 + (1 if len(list_x) % 2 == 1 else 0))):
    list_y.append(list_x[i] * list_x.pop())
print(f"Произведение пар чисел: {list_y}")

print("---------------------------------")

# 3.

list_x = list(map(float, input("Введите вещественные числа через пробел: ").split(" ")))
list_y = []

for i in list_x:
    if i % 1 != 0:
       list_y.append(round(i % 1, 2))

print(f"Разницу между максимальным и минимальным значением: {max(list_y) - min(list_y)}")

print("---------------------------------")

# 4.

def decbin(i):
    if i == 0:
       print(i)
       return
    elif i != 1:
       decbin(i // 2)
    print(i % 2, end="")

decbin(int(input("Введите десятичное число: ")))

print(" - двоичное число")
print("---------------------------------")

# 5.

def negafibonacci(n):
    if n == 0 or n == 1:
       return n
    if n == -1:
       return -n
    if n < 0:
       return round(negafibonacci(abs(n)) * (-1)**(n + 1))
    else:
       return negafibonacci(n - 1) + negafibonacci(n - 2)

n = int(input("Введите сколько элементов из негафиббоначчи вывести: "))
temp = []

for i in range(-n, n + 1):
    temp.append(negafibonacci(i))

print(temp)