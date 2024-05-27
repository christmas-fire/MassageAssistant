from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_start() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Запустить бота", callback_data="start")]
        ]
    )
    return kb
