from aiogram import types


async def color_menu(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Duo(2)", callback_data="duo"),
        types.InlineKeyboardButton(text="Classic(3)", callback_data="classic"),
        types.InlineKeyboardButton(text="Big(4)", callback_data="big"),
        types.InlineKeyboardButton(text="Giant(5)", callback_data="giant"),
        types.InlineKeyboardButton(text=" ⬅Menu⬅", callback_data="games")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await call.message.edit_text("Choice your game mode", reply_markup=keyboard)
