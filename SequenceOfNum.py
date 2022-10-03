# 3) Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# Для n = 5: сумма = 11,55

n = int(input('Enter positive number: '))

sum = 0
for i in range(1, n+1):
    sum += (1 + (1/i)**i)

print(round(sum, 2))
