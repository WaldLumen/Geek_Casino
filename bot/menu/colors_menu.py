from aiogram import types


async def colors_menu(edit_message: types.CallbackQuery.message.edit_text):
    buttons = [
        types.InlineKeyboardButton(text="Duo(2)", callback_data="duo"),
        types.InlineKeyboardButton(text="Classic(3)", callback_data="classic"),
        types.InlineKeyboardButton(text="Big(4)", callback_data="big"),
        types.InlineKeyboardButton(text="Giant(5)", callback_data="giant"),
        types.InlineKeyboardButton(text=" ⬅Menu⬅", callback_data="games")
    ]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)

    await edit_message("Choice your game mode", reply_markup=keyboard)
