from random import randint as r

def you_func(name):
    taken_candy = int(
        input(f"{name} сколько конфет хочешь забрать от 1 до 28? "))
    while taken_candy < 1 or taken_candy > 28:
        taken_candy = int(input(f"{name} попробуй еще раз. От 1 до 28! "))
    return taken_candy

def bot_func(candy):
    random = r(1, 29)
    while candy - random <= 28 and candy > 29:
        random = r(1, 29)
    return random

print('--- Настройка ---')

player1 = input("Напиши свое имя: ")
candy = int(input("Укажи количество конфет: "))

game = int(
    input("1 - бот, 2 - друг. С кем будем играть? "))
if game < 1 or game > 2:
    game = r(0, 2)
    if game == 1:
        print(f"{player1} играет с ботом")
    elif game == 2:
        print(f"{player1} играет с другом")
if game == 1:
    player2 = "Бот"
elif game == 2:
    player2 = input("Имя друга: ")

print('--- Игра ---')

step = r(0, 2)
print(f"{player1 if step == 1 else player2} ходит первым!")

while candy > 28:
    if game == 1:
        taken = you_func(player1) if step == 1 else bot_func(candy)
    elif game == 2:
        taken = you_func(player1) if step == 1 else you_func(player2)
    candy -= taken
    step += 1 if step < 1 else -1
    print(f"{player2 if step == 1 else player1} взял {taken} конфет. Осталось {candy}.")
print(f'Победил: {player1 if step == 1 else player2}, забрав последние {candy} конфет. {player2 if step == 1 else player1} проиграл.')