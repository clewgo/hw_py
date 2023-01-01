# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

def in_number(in_text):
    truefalse = False
    while not truefalse:
        try:
            num = int(input(f"{in_text}"))
            truefalse = True
        except ValueError:
            print("Это не число")
    return num


def check_num(num):
    if 6 <= num <= 7:
        print("Ура! Выходной")
    elif 0 < num < 6:
        print("Рабочий день")
    else:
        print("Число должно быть больше 1 и меньше 7")


num = in_number("Введите число, обозначающее день недели: ")
check_num(num)

# 2. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным