import asyncio
import logging
import sys

from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode


load_dotenv()

TOKEN = getenv("BOT_TOKEN")
ADMIN = getenv("ADMIN")

bot = Bot(TOKEN)
dp = Dispatcher()
pm = ParseMode.HTML


@dp.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.username}!")


@dp.message(Command(commands=["get_id"]))
async def command_get_id_handler(message: Message) -> None:
    await bot.send_message(
        chat_id=ADMIN,
        text=f"ID пользователя @{message.from_user.username}: {html.code(message.chat.id)}",
        parse_mode=pm,
    )


@dp.message()
async def echo_handler(message: Message) -> None:
    await message.send_copy(chat_id=message.chat.id)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
