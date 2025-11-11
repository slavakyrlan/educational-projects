"""
Coroutines (Корутины) — это функции, которые могут быть приостановлены
 и возобновлены. Они позволяют контролировать моменты своей
 приостановки и возобновления работы, что делает их идеальными для
 сценариев асинхронного программирования, например, при выполнении
 длительных задач, ожидании данных от внешних ресурсов или выполнении
 других корутин.
"""

import asyncio
import time
async def example_coroutine(n):
    print(f"Hello from coroutine #{n}! {time.perf_counter() - start:.3f} секунды")
    await asyncio.sleep(1)
    print(f"Coroutine #{n} completed! {time.perf_counter() - start:.3f} секунды")
async def main():
    for num in range(1, 11):
        await example_coroutine(num)
start = time.perf_counter()
asyncio.run(main())
print(f"Программа выполнена за {time.perf_counter() - start:.3f} секунды")


#  2
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
async def main():
    await count()
asyncio.run(main())


#  3
import asyncio
async def main():
    print('Hello, Asyncio!')
asyncio.run(main())


#  4
import asyncio
async def coro_1():
    print('coro_1 says, hello coro_2!')
async def coro_2():
    print('coro_2 says, hello coro_1!')
async def main():
    await coro_1()
    await coro_2()
asyncio.run(main())


#  5
import asyncio
async def generate(num):
    print(f"Корутина generate с аргументом {num}")
async def main():
    for x in range(10):
        await generate(x)
asyncio.run(main())


#  6
import asyncio
async def coro_1():
    print("Вызываю корутину 0")
async def coro_5():
    print("Вызываю корутину 3")
    await coro_3()
async def coro_3():
    print("Вызываю корутину 2")
    await coro_2()
async def coro_4():
    print("Вызываю корутину 1")
    await coro_1()
async def coro_2():
    print("Вызываю корутину 4")
    await coro_4()
asyncio.run(coro_5())
