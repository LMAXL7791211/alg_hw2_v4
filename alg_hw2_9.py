#  9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
#  Вывести на экран это число и сумму его цифр.

q = int(input('Введите количество чисел -->'))
max_sum_dig = 0

for i in range(q):
    num = input(f'Введите {i + 1}-е число -->')
    num_int = int(num)
    sum_d = 0
    while num_int > 0:
        sum_d += num_int % 10
        num_int //= 10
    if max_sum_dig < sum_d:
        max_sum_dig = sum_d
        max_n = num

print(f'Число, наибольшее по сумме цифр = {max_n} ; сумма его цифр = {max_sum_dig} .')