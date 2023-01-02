from aiogram import types

from tgbot.bot.Banque import Banque


async def main_menu(message: types.Message):
    bank = Banque()

    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="👤Profile👤", callback_data="profile"),
                 types.InlineKeyboardButton(text="⭐Start Game⭐", callback_data="games"),
                 # here I will add top of the richest players
                 types.InlineKeyboardButton(text="🔝Not available now🔝", callback_data="f"))

    bank.register_user(user_id=user_id)

    await message.answer("Welcome. This is main menu of this bot,"
                         "here you can check your profile or start playing.", reply_markup=keyboard)
