# 1.
# пара-ра-рам рам-пам-папам па-ра-па-да

print("Парам пам-пам" if len(set(map(lambda x: sum(i in {
      "аоиыуэюяё"} for i in x), input().lower().split()))) == 1 else "Пам парам")

print("---------------------------------")

# 2.

a = int(input("Укажите количество строк: \n"))
b = int(input("Укажите количество столбцов: \n"))

def print_operation_table(f, h, w):
    for i in range(1, h + 1):
        print(*(f(i, k) for k in range(1, w + 1)))

print_operation_table(lambda x, y: x * y, a, b)

print("---------------------------------")

# 3.

def same_by(characteristic, objects):
    res = list(map(characteristic, objects))
    print(f"lambda x: x % 2, {for_same_by} --> {all([i == res[0] for i in res])}")

for_same_by = [2, 4, 6, 8]
same_by(lambda x: x % 2, for_same_by)

for_same_by = [2, 4, 5, 7]
same_by(lambda x: x % 2, for_same_by)