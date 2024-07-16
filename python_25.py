import asyncio
import time

start = time.time() ## точка отсчета времени

async def hello():
    print('Запуск функции hello')
    await asyncio.sleep(5)  # Отдаем управление обратно в Event loop пока ждём
    print('Переключение контекста в функцию hello')


async def starter():
    await asyncio.gather(*[hello() for i in range(5000)])

asyncio.run(starter())

end = time.time() - start
print(end)