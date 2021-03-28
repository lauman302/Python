'''Напишите программу, которая считывает список чисел lst из 
первой строки и число x из второй строки, которая выводит 
все позиции, на которых встречается число x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в 
списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию 
абсолютного значения'''

# put your python code here
nums = [int(i) for i in input().split()]  # получаем список чисел из строки
needed = int(input())  # искомое значение
if needed not in numbers:  # если искомое значение отсутствует, то
    print("Отсутствует")  # вывести слово
else:
    [print(i, end=" ") for i, x in enumerate(numbers) if x == needed]  # если искомое значение есть, вывести индексы