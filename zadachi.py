# 1 задача

#x = int(input('Введите число для проверки на простоту: '))
#z = 0
#for i in range(2, x // 2+1):
#    if (x % i == 0):
#        z += 1
#if (z <= 0):
#    print('Число является простым')
#else:
#    print('Число не является простым')




# задача 2

#def sortirovka(massiv):
#   n = len(massiv)
#    for i in range(n):
#        min_znach = i
#        for x in range(i + 1, n):
#            if massiv[x] < massiv[min_znach]:
#                min_znach = x
#        massiv[i], massiv[min_znach] = massiv[min_znach], massiv[i]
#List = [353, 3672, 464, 2, 4343, 674, 968, 8]
#sortirovka(List)
#print(f'Отсортированный массив чисел: {List}')




# задача 3

#def ischem_max_znach(massiv):
#    if len(massiv) == 0:
#        return None
#    max_znach = massiv[0]
#    for i in massiv:
#        if i > max_znach:
#            max_znach = i
#    return max_znach
#List = [23, 34524, 32, 3, 75, 5777]
#max_znach = ischem_max_znach(List)
#print(f'максимальное значение в массиве: {max_znach}')




# задача 4

#n = int(input('Введите число, для расчета числа фибоначи:'))
#def fib(n):
#    if n <= 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return fib(n - 1) + fib(n - 2)
#result = fib(n - 1)
#print(f'число фибоначи: {result}')




# задача 5

#def chast_vstr_str(massiv):
#    if len(massiv) == 0:
#        return None  # Возвращаем None, если массив пустой
#    rasschit_str = {}  # Создаем словарь для подсчета частоты строк
#    x = None
#    d = 0
#    for i in massiv:
#        if i in rasschit_str:
#            rasschit_str[i] += 1
#        else:
#            rasschit_str[i] = 1
#        if rasschit_str[i] > d:
#            d = rasschit_str[i]
#            x = i
#    return x
#List = ['https', 'fja', 'ecbsi', 'https']
#x = chast_vstr_str(List)
#print(f'наиболее часто встречающаяся строка: {x}')