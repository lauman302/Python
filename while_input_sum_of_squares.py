'''Напишите программу, которая считывает с консоли числа (по одному в строке) 
до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после 
этого выводит сумму квадратов всех считанных чисел.

Гарантируется, что в какой-то момент сумма введённых чисел окажется 
равной 0, после этого считывание продолжать не нужно.

В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент 
замечаем, что сумма этих чисел равна нулю и выводим сумму их квадратов, 
не обращая внимания на то, что остались ещё не прочитанные значения.'''

nums = [int(input())] # сохраняем в переменной первое значение
while sum(nums) != 0: # запускаем цикл с условием, что сумма значений в переменной не равно 0
    nums.append(int(input())) # добавляем новое число в список
res = [abs(i) ** 2 for i in s] # возведем в квадрат ка
print(sum(res)) # вывод результат