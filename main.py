import asyncio
import logging
import sys

from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


load_dotenv()

TOKEN = getenv("BOT_TOKEN")
ADMIN = getenv("ADMIN")

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.username}!")


@dp.message(Command(commands=["get_id"]))
async def command_get_id_handler(message: Message, bot: Bot) -> None:
    await bot.send_message(
        chat_id=ADMIN,
        text=f"ID пользователя @{message.from_user.username}: {message.chat.id}",
    )


@dp.message()
async def echo_handler(message: Message) -> None:
    await message.send_copy(chat_id=message.chat.id)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
