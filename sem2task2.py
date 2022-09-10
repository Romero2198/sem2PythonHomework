n = int(input('Введите число: '))
mult = 1
i = 1
print(f'{n} ->', end = ' ')
while i <= n:
    mult *= i
    i += 1
    print(mult, end = ' ')