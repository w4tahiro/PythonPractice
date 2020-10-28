import random

def a():
    pal[0] = int(input("1つ目"))
    pal[1] = int(input("2つ目"))
    pal[2] = int(input("3つ目"))

def calc():
    hit = 0
    blow = 0
    for i in range(3):
        for j in range(3):
            if pal[i] == ans[i]:
                hit = hit + 1
                break
            elif i != j:
                if pal[i] == ans[j]:
                    blow = blow + 1
    return hit,blow

pal = [0,0,0]
ans = [0,0,0]
ans = random.sample(range(10),3)
flag = 1
while flag == 1:
    a()
    reshit,resblow = calc()
    print(resblow,"blow",reshit,"hit")
    if reshit == 3:
        print("おわり")
        flag = 0


