WHITE = 0
BLACK = 1
def end_check():
    w = 0
    b = 0
    e = 0
    for i in range(8):
        for j in range(8):
            if cell[i][j] == None:
                e = 1
            elif cell[i][j] == 0:
                w = 1
            elif cell[i][j] == 1:
                b = 1
    if b == 0 or w == 0 or e == 0:
        return 1
    else:
        return 0

def show_board():
    print("  0 1 2 3 4 5 6 7")
    for i in range(8):
        print(i,end =" ")
        for j in range(8):
            if cell[i][j] == 0:
                print("W",end=" ")
            elif cell[i][j] == 1:
                print("B",end=" ")
            else:
                print("*",end=" ")
        print("\n",end="")

def turn_over2(x,y,zx,zy,turn):
    if turn == 0:
        cnt = 0
        ttt = 0
        wx = x
        wy = y
        while wx + zx >= 0 and wx + zx <= 7 and wy + zy >= 0 and wy + zy <= 7:
            wx = wx + zx
            wy = wy + zy
            if cell[wx][wy] == 1:
               cnt = cnt + 1
            elif cnt >= 1 and cell[wx][wy] == 0:
                ttt = 1
                break
            else:
                break
        if ttt == 1:
            if cnt == 0:
                return 0
            else:
                cell[x][y] = 0
                while cnt >= 1:
                    x = x + zx
                    y = y + zy
                    cell[x][y] = 0
                    cnt = cnt - 1
                return 1
        else:
            return 0

    elif turn == 1:
        cnt = 0
        ttt = 0
        wx = x
        wy = y
        while wx + zx >= 0 and wx + zx <= 7 and wy + zy >= 0 and wy + zy <= 7:
            wx = wx + zx
            wy = wy + zy
            if cell[wx][wy] == 0:
               cnt = cnt + 1
            elif cnt >= 1 and cell[wx][wy] == 1:
                ttt = 1
                break
            else:
                break
        if ttt == 1:
            if cnt == 0:
                return 0
            else:
                cell[x][y] = 1
                while cnt >= 1:
                    x = x + zx
                    y = y + zy
                    cell[x][y] = 1
                    cnt = cnt - 1
                return 1
        else:
            return 0

def turn_over(x,y,turn):
    tf = 0
    if x >= 0 and x <= 7 and y >= 0 and y <= 7:
        if cell[x][y] == None:
            if turn == 0:
                tf = tf + turn_over2(x,y,-1,0,turn)
                tf = tf + turn_over2(x,y,-1,-1,turn)
                tf = tf + turn_over2(x,y,-1,1,turn)
                tf = tf + turn_over2(x,y,0,1,turn)
                tf = tf + turn_over2(x,y,0,-1,turn)
                tf = tf + turn_over2(x,y,1,0,turn)
                tf = tf + turn_over2(x,y,1,1,turn)
                tf = tf + turn_over2(x,y,1,-1,turn)
                print(tf)
            elif turn == 1:
                tf = tf + turn_over2(x,y,-1,0,turn)
                tf = tf + turn_over2(x,y,-1,-1,turn)
                tf = tf + turn_over2(x,y,-1,1,turn)
                tf = tf + turn_over2(x,y,0,1,turn)
                tf = tf + turn_over2(x,y,0,-1,turn)
                tf = tf + turn_over2(x,y,1,0,turn)
                tf = tf + turn_over2(x,y,1,1,turn)
                tf = tf + turn_over2(x,y,1,-1,turn)
                print(tf)
            if tf == 0:
                return 0
            else:
                return 1
        else:
            print("おけない！")
            return 0
    else:
        print("0～7まで")
        return 0

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
    print("--"*9)
    show_board()
    if end_check() == 1:
        break
    #ひっくり返す処理
    while a == 0:
        if turn == 1:
            print("black")
        elif turn == 0:
            print("white")

        tmp = int(input("tate(0～7,pass:9)"))
        tmp2 = int(input("yoko(0～7,pass:9)"))
        #ひっくり返せたらブレイク
        if tmp == 9 and tmp2 == 9:
            print("パス")
            break
        else:
            if turn_over(tmp,tmp2,turn) >= 1:
                break
            print("おけない")
    #ターン変更
    turn = turn_change(turn)

b = 0
w = 0
for i in range(8):
    for j in range(8):
        if cell[i][j] == 0:
            w = w + 1
        elif cell[i][j] == 1:
            b = b + 1

if b > w:
    print("黒の勝ち")
elif w > b:
    print("白の勝ち")
elif w == b:
    print("引き分け")

print("試合終了")
