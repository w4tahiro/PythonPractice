def hello():
    print("Hello")
    return 3

def hello2():
    hello()
    hello3()

def hello3():
    print("Hello3")

hello2()

a = 1 + hello()

print(a)
