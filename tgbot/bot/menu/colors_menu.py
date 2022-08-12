from aiogram import types


async def color_menu(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    colors_menu = ["Duo(2)", "Classic(3)", "Big(4)", "Giant(5)", "⬅Menu⬅"]

    for color in colors_menu:
        keyboard.add(types.InlineKeyboardButton(text=color, callback_data=color))

    await call.message.edit_text("Choice your game mode", reply_markup=keyboard)
