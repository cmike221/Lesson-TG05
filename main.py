import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Вот в этом промежутке мы будем работать и писать новый код
def fetch_yes_no_gif(req):
    # Отправляем GET-запрос к API
    print(f'https://yesno.wtf/api?force={req}')
    response = requests.get(f'https://yesno.wtf/api?force={req}')

    # Проверяем, успешен ли запрос
    if response.status_code == 200:
        data = response.json()  # Получаем JSON-ответ
        gif_picture = data['image']  # Извлекаем URL GIF
        return gif_picture
    else:
        print('Error:', response.status_code)
        return None


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Отправь /yes /no /maybe - получишь случайную гифку")


@dp.message(Command("help"))
async def gif_help(message: Message):
    await message.answer("Доступны команды /yes /no /maybe - получишь случайную гифку")


@dp.message(Command("yes"))
async def gif_yes(message: Message):
    req = "yes"
    gifka = fetch_yes_no_gif(req)
    if gifka:
        await message.answer_photo(photo=gifka)
    else:
        await message.answer("Что-то пошло не так ...")


@dp.message(Command("no"))
async def gif_no(message: Message):
    req = "no"
    gifka = fetch_yes_no_gif(req)
    if gifka:
        await message.answer_photo(photo=gifka)
    else:
        await message.answer("Что-то пошло не так ...")


@dp.message(Command("maybe"))
async def gif_maybe(message: Message):
    req = "maybe"
    gifka = fetch_yes_no_gif(req)
    if gifka:
        await message.answer_photo(photo=gifka)
    else:
        await message.answer("Что-то пошло не так ...")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
