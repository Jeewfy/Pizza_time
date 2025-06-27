import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv, find_dotenv
from loguru import logger


load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')


async def main():
    logger.add('file.log',
               format='{time:YYYY-MM-DD at HH-mm-ss} | {level} | {message}',
               rotation='3 days',
               backtrace=True,
               diagnose=True)

    bot = Bot(token=TOKEN)
    logger.info('Бот создан.')
    dp = Dispatcher()
    logger.info('Диспетчер создан.')

    @dp.message(Command('start'))
    async def start_command(message: types.Message):
        await message.answer('Здесь должно быть приветствие, ну да ладно')
        logger.info('Бот ответил на команду "start".')

    @dp.message()
    async def echo(message: types.Message):
        await message.reply(message.text)
        logger.info('Бот возвратил сообщение пользователя.')

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
