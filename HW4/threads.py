# Задание №7
# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи использовать многопоточность.
# В каждом решении нужно вывести время выполнения вычислений.

from random import randint
import threading
import time

summ_list = 0

def summ(part_list):
    global summ_list
    for num in part_list:
        summ_list += num

my_list = [randint(1, 100) for _ in range(1000000)]
start_time = time.time()

threads = []
parts = 20

for i in range(parts):
    t = threading.Thread(target=summ(my_list[(len(my_list) // parts) * i:len(my_list) // parts * (i + 1)]))
    threads.append(t)
    t.start()
t = threading.Thread(target=summ(my_list[:len(my_list) % parts]))
threads.append(t)
t.start()

for t in threads:
    t.join()

print(f"Сумма: {summ_list}")
print(f"Время выполнения {time.time() - start_time:.2f} секунд")