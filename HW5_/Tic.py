#Игра в крестики и нолики 
board = range(1,10)
def draw_board(board):
    print("-------------")
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-------------")
def single(player):
    board=[" " for i in range(9)]
    playerprop = {'X': [], 'O' : []} # словарь с ключами X и O, где храняться позиции


def newinput(stok):
    while True:
        print("Where do you want to put : ", end="") 
        try:
            gap=int(input())    
        except :
              print("Invalid Input!!! Try Again")
              continue
        if gap >=1 and gap<=9:
            if (str(board[gap-1]) not in "XO"):
                board[gap-1] = stok
                valid = True
            else:
               print("Invalid Input!!! Try Again") 
        else: 
            print("Oops! The Place is already occupied. Try again!!") 

def win(board):
     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
     for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
     return False

def main(board):
    counter = 0
    nwin = False
    while not nwin:
        draw_board(board)
        if counter % 2 == 0:
            newinput("X")
        else:
            newinput("O")
        counter += 1
        if counter > 4:
            tmp = win(board)
            if tmp == True:
                print(tmp, "WIN!")
                nwin = True
                break
        if counter == 9:
            print ("No winner ")
            break
    draw_board(board)    

main(board)  