a = input('Введите вещественное число: ')
sum = 0
for i in a:
    if i != ".":
        sum += int(i)
print(sum)