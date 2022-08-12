from aiogram import types


async def to_main_menu(call: types.CallbackQuery):
    # main menu
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="👤Profile👤", callback_data="profile"),
                 types.InlineKeyboardButton(text="⭐Start Game⭐", callback_data="games"),
                 types.InlineKeyboardButton(text="🔝Top🔝", callback_data="f"))

    await call.message.edit_text("Welcome. This is main menu of this bot,"
                                 "here you can check your profile or start playing.", reply_markup=keyboard)


async def to_help_menu(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="Games Base Information", callback_data="g_b_i")
    ]

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)

    await call.message.edit_text("Hello, I'm your informant, what do you want to know?", reply_markup=keyboard)
