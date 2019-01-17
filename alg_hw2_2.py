#  2. Посчитать четные и нечетные цифры введенного натурального числа.
#  Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

"""
# цикл

n = int(input('Введите натуральное число-->'))

even = 0
odd = 0

while n != 0:
    if (n % 10) % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10
print(f'В числе {even} четных и {odd} нечетнх цифр')

"""

#рекурсия

def count_digit(number, ev, od):
    if number == 0:
        return ev, od
    else:
        return count_digit(number // 10, ev + abs((number % 10) % 2 - 1), od + (number % 10) % 2)


n = int(input('Введите натуральное число-->'))

even, odd = count_digit(n, 0, 0)

print(f'В числе {even} четных и {odd} нечетных цифр')