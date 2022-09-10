from math import pow
k = int(input('Введите число: '))
i = 1
count = 0
sum = 0
while i <= k:
    count = pow((1 + 1/i), i)
    sum += count
    i += 1
print(sum)