from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def keyboard_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите команду",
        keyboard=[
            [KeyboardButton(text="/get_id"), KeyboardButton(text="/casino")]
        ]
    )
    return kb