from random import randint


n = int(input('Введите число: '))
i = 0
s = []
while i < n:
    s.append(randint(-n, n))
    i += 1
print(s)