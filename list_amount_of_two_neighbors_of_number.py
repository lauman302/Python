'''Напишите программу, на вход которой подаётся список чисел одной строкой. 
Программа должна для каждого элемента этого списка вывести сумму двух его 
соседей. Для элементов списка, являющихся крайними, одним из соседей 
считается элемент, находящий на противоположном конце этого списка. 
Например, если на вход подаётся список "1 3 5 6 10", то на выход 
ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.'''

# put your python code here
nums = [int(num) for num in input().split()]  # получаем на вход строку с числами
if len(nums) == 1:  # если количество элементов в списке равно - 1
    print(nums[0])  # вывести это значение
else:
    for i in range(0, len(nums) - 1):  # воспользуемся циклом
        print(nums[i - 1] + nums[i + 1], end=' ')  # вывести сумму двух соседей элемента
    print(nums[len(nums) - 2] + nums[0])  # вывести сумму для последнего элемента из списка