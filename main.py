import asyncio
import logging
import sys

from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html, types, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode

from Default_commands import *
from Inline_handler import *
from Keyboard_handler import *

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
ADMIN = getenv("ADMIN")
RAZVAL = getenv("RAZVAL")

bot = Bot(TOKEN)
dp = Dispatcher()
pm = ParseMode.HTML


@dp.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Hello, {message.from_user.username}!", reply_markup=keyboard_start()
    )


@dp.message(Command(commands=["get_id"]))
async def command_get_id_handler(message: Message) -> None:
    await message.answer(
        text=f"ID пользователя @{message.from_user.username}: {html.code(message.chat.id)}",
        parse_mode=pm,
    )


@dp.message(Command(commands=["casino"]))
async def command_casino(message: Message) -> None:
    picture = types.FSInputFile("images/casino.jpg")
    text = "Испытай удачу!"
    await message.answer_photo(picture, text, reply_markup=inline_casino())
    

@dp.message(Command(commands=["razval"]))
async def command_razval(message: Message) -> None:
    await bot.send_message(chat_id=RAZVAL, text="Если заработает, я ахуею)\n\nР.S. Я пытаюсь отправить тебе сообщение напрямую через бота, зная твой id.\n\nЛюблю тебя, моя милая развал!")


@dp.callback_query(F.data.startswith("casino_"))
async def callback_casino(callback: CallbackQuery):
    action = callback.data.split("_")[1]

    if action == "dice":
        await callback.message.answer_dice(emoji="🎲")
    elif action == "football":
        await callback.message.answer_dice(emoji="⚽")
    elif action == "darts":
        await callback.message.answer_dice(emoji="🎯")
    elif action == "backetball":
        await callback.message.answer_dice(emoji="🏀")
    elif action == "slots":
        await callback.message.answer_dice(emoji="🎰")

    await callback.answer()


@dp.message()
async def echo_handler(message: Message) -> None:
    await message.send_copy(chat_id=message.chat.id)


async def main() -> None:
    await set_bot_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
