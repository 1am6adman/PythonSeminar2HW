###Ex10



# n = int(input('Введите количество монет '))
# o = r = 0
# for i in range(n):
#     x = int(input('Орел(1) или решка(0)? '))
#     if x == 1:
#         o += 1
#     else:
#         r += 1
# if o < r:
#     print(f'Переверните {o} монет с орла на решку, их меньше всего')
# elif o == r:
#     print(f'Количество орлов и решек одинаково, по {o} штук')
# else:
#     print((f'Переверните {r} монет с решки на орла, их меньше всего'))


###Ex12


# x = abs(int(input('Введите первое натуральное число от 1 до 1000 ')))
# y = abs(int(input('Введите второе натуральное число от 1 до 1000 ')))
# if x < 1 or x > 1000 or y < 1 or y > 1000:
#     print('Вы ввели число вне заданного диапазона')
# else:
#     S = x + y
#     P = x * y
#     stop = 0
#     for i in range(1001):
#         if stop != 1:
#             for j in range(1001):
#                 if stop != 1:
#                     if i * j == P and i + j == S:
#                         print(i, j)
#                         stop = 1
#             else:
#                 j = 1001
#         else:
#             i = 1001