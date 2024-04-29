# Задание №7
# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи использовать многопроцессорность.
# В каждом решении нужно вывести время выполнения вычислений.

from random import randint
import multiprocessing
import time

counter = multiprocessing.Value('i', 0)

def summ(part_list, cnt):
    for num in part_list:
        with cnt.get_lock():
            cnt.value += num


if __name__ == '__main__':
    my_list = [randint(1, 100) for _ in range(1000000)]
    processes = []
    parts = 20

    start_time = time.time()

    for i in range(parts):
        p = multiprocessing.Process(target=summ(my_list[(len(my_list) // parts) * i:len(my_list) // parts * (i + 1)], counter))
        processes.append(p)
        p.start()
    p = multiprocessing.Process(target=summ(my_list[:len(my_list) % parts], counter))
    processes.append(p)
    p.start()

    for p in processes:
        p.join()

    print(f"Сумма: {counter.value}")
    print(f"Время выполнения {time.time() - start_time:.2f} секунд")