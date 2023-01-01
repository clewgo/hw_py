# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным


def in_number_1(in_text):
    truefalse = False
    while not truefalse:
        try:
            num = int(input(f"{in_text}"))
            truefalse = True
        except ValueError:
            print("Это не число")
    return num


def check_1(num):
    if 6 <= num <= 7:
        print("Ура! Выходной")
    elif 0 < num < 6:
        print("Рабочий день")
    else:
        print("Число должно быть от 1 до 7 включительно")


num = in_number_1("Введите число, обозначающее день недели: ")
check_1(num)


print("---------------------------------")

# 1. Напишите программу для проверки истинности утверждения -(X ⋁ Y ⋁ Z) = -X ⋀ -Y ⋀ -Z для всех значений предикат


def in_number_2(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите число {xyz[i]}: "))
    return a


def check_2(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    res = left == right
    return res


st = in_number_2(3)

if check_2(st) == True:
    print(f"Это утверждение верно")
else:
    print(f"Это утверждение ложно")


print("---------------------------------")

# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)


def in_number_3(x):
    a = [0] * x
    for i in range(x):
        truefalse = False
        while not truefalse:
            try:
                number = float(input(f"Введите {i+1}-ю координату: "))
                a[i] = number
                truefalse = True
                if a[i] == 0:
                    truefalse = False
                    print("Координата не должно быть равна 0")
            except ValueError:
                print("Введите число!")
    return a


def check_3(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")


kd = in_number_3(2)
check_3(kd)


print("---------------------------------")

# 1. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)


in_number_4 = float(input('Введите номер четверти: '))

if in_number_4 == 1:
    print('Диапазон координат: X > 0 и Y > 0')
elif in_number_4 == 2:
    print('Диапазон координат: X < 0 и Y > 0')
elif in_number_4 == 3:
    print('Диапазон координат: X < 0 и Y < 0')
elif in_number_4 == 4:
    print('Диапазон координат: X > 0 и Y < 0')
else:
    print('Нет четверти')


print("---------------------------------")

# 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве


def inum(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        truefalse = False
        while not truefalse:
            try:
                numb = int(input(f"Введите координату {xy[i]}: "))
                a.append(numb)
                truefalse = True
            except ValueError:
                print("Введите целое число")
    return a


def calc_len(a, b):
    length = ((b[0] - a[0])**2 + (b[1] - a[1])**2)**(0.5)
    return length


print("Точка с координатами 'А'")
point_a = inum(2)
print("Точка с координатами 'B'")
point_b = inum(2)

print(f"Длина разреза: {format(calc_len(point_a, point_b), '.3f')}")