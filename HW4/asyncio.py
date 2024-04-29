# Задание №7
# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи использовать асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.

from random import randint
import asyncio
import time

my_list = [randint(1, 100) for i in range(1000000)]
summ_list = 0


async def summ(part_list):
    global summ_list
    for num in part_list:
        summ_list += num

async def main():
    tasks = []
    parts = 20
    for i in range(parts):
        task = asyncio.create_task(summ(my_list[(len(my_list) // parts) * i:len(my_list) // parts * (i + 1)]))
        tasks.append(task)
    task = asyncio.create_task(summ(my_list[(len(my_list) // parts) * parts:]))
    tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    
    print(f"Сумма: {summ_list}")
    print(f"Время выполнения {time.time() - start_time:.2f} секунд")