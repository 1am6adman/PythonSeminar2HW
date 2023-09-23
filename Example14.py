n = abs(int(input('Введите число n ')))
stop = 0
P = 2
for i in range(n):
    if stop != 1:
        P = P ** i
        if P <= n:
            print(P, end=' ')
            P = 2
        else:
            stop = 1
    else:
        i = n