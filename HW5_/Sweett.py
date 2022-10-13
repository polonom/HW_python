import random
print("Добро пожаловать в игру!На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
countcandies=[0,0]
turn = random.randrange(0,2)
allcandies=2021
counter1 = 0 
counter2 = 0
if turn:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")


def ModernConditions():
    print("Количество конфет на столе: ", allcandies )
    print(f"У первого игрока: {counter1} конфет.\tУ второго игрока: {counter2} конфет")

def PlayerTake(name):
        number=int(input(f"{name} ходит. Какое количество конфет, вы возьмете? "))
        if number > 0 and number <= allcandies and number <= 28: return number
        else: 
            print('ooooooppppps! Try again') 
            


while allcandies > 28:
        ModernConditions()
        if turn:
           newturn = PlayerTake(player1)
           counter1+=newturn
           allcandies -= newturn
           turn=False
        else:
            newturn = PlayerTake(player2)
            counter2+=newturn
            allcandies -= newturn
            turn=True
        if allcandies == 0 : 
            break

if turn:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")        


    


