# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока 
# делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все 
# конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все 
# конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


from random import randint

def lottery(people1,people2):    
    while True:
        if people1 > people2:
            return 'people1'
            break
        if people2 > people1:
            return 'people2' 
            break

player = lottery(randint(0,10),randint(0,10))
print(f'Начинает игрок: {player}')
candy = int(2021)
while candy > 0:
    print(f'Осталось {candy} ')
    if player == 'people1':
        candy = candy - int(input('Сколько конфет берет первый игрок? '))
        player = 'people2'
    else:
        candy = candy - int(input('Сколько конфет берет второй игрок?'))
        player = 'people1'
print(f'Победил {player}')        