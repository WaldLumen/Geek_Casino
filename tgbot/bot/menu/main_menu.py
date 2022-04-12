# main menu
from aiogram import types

from tgbot.bot.DataBase import DBQueries

requests = DBQueries()


async def main_menu(message: types.Message):
    # main menu
    user_id = message.from_user.id
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Profile", callback_data="profile"),
                 types.InlineKeyboardButton(text="Start Game", callback_data="games"),
                 types.InlineKeyboardButton(text="Top", callback_data="f"))

    requests.register_user(user_id=user_id)

    await message.answer("Hello from Sylvia", reply_markup=keyboard)
