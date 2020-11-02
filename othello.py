WHITE = 0
BLACK = 1
def show_board():
    for i in range(8):
        for j in range(8):
            if cell[i][j] == 0:
                print("W",end=" ")
            elif cell[i][j] == 1:
                print("B",end=" ")
            else:
                print("*",end=" ")
        print("\n",end="")

def check_able(a,b):
    print("yeah")

def turn_change(a):
    if a == 0:
        return 1
    elif a == 1:
        return 0

cell = [[None]*8 for i in range(8)]
cell[3][3] = WHITE
cell[3][4] = BLACK
cell[4][3] = BLACK
cell[4][4] = WHITE
flag = 1
turn = 0
a = 0

#本体
while flag == 1:
    show_board()
    check = check_able()
    #まずおける場所があるかチェック
    if check == 1:
        #1人目おけないからターン変更
        turn = turn_change(turn)
    elif check == 2:
        #2人ともおけないからゲーム終了
        flag = 0
        break
    #ひっくり返す処理
    while a == 0:
        tmp = int(input("縦"))
        tmp2 = int(input("横"))
        #ひっくり返せたらブレイク
        if turn_over(tmp,tmp2) == 1:
            break
    #ターン変更
    turn = turn_change(turn)

    
    
    show_board()
