# games menu
from aiogram import types


async def menu_games(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="🎲Dices🎲", callback_data="dices"),
        types.InlineKeyboardButton(text="Colors", callback_data="colors_menu"),
        types.InlineKeyboardButton(text="Not available now", callback_data="c"),
        types.InlineKeyboardButton(text="Not available now", callback_data="c"),
        types.InlineKeyboardButton(text=" ⬅Menu⬅", callback_data="to_menu")
    ]

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)

    await call.message.edit_text("To get detailed information about the minigame click on it", reply_markup=keyboard)
