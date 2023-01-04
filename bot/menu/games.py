from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


async def menu_games(edit_message: CallbackQuery.message.edit_text):
    buttons = [
        InlineKeyboardButton(text="🎲Dices🎲", callback_data="dices"),
        InlineKeyboardButton(text="Colors", callback_data="colors_menu"),
        # lottery game
        InlineKeyboardButton(text="Not available now", callback_data="cum"),
        # I don`t have any ideas for this game
        InlineKeyboardButton(text="Not available now", callback_data="pot"),
        InlineKeyboardButton(text=" ⬅Menu⬅", callback_data="to_menu")
    ]

    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)

    await edit_message("To get detailed information about the minigame click on it", reply_markup=keyboard)
