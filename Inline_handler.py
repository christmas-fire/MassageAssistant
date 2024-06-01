from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_start() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Запустить бота", callback_data="start")]
        ]
    )
    return kb


def inline_casino() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎲бросить кости", callback_data="casino_dice")],
            [
                InlineKeyboardButton(
                    text="⚽️футбольное пенальти", callback_data="casino_football"
                )
            ],
            [InlineKeyboardButton(text="🎯игра в дартс", callback_data="casino_darts")],
            [
                InlineKeyboardButton(
                    text="🏀бросок в кольцо", callback_data="casino_backetball"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎰игровой автомат", callback_data="casino_slots"
                )
            ],
        ]
    )
    return kb
