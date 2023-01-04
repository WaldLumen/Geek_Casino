from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


async def to_main_menu(edit_message: CallbackQuery.message.edit_text):
    # main menu
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton(text="👤Profile👤", callback_data="profile"),
                 InlineKeyboardButton(text="⭐Start Game⭐", callback_data="games"),
                 InlineKeyboardButton(text="🔝Top🔝", callback_data="f"))

    await edit_message("Welcome. This is main menu of this bot,"
                                 "here you can check your profile or start playing.", reply_markup=keyboard)


async def to_help_menu(edit_message: CallbackQuery.message.edit_text):
    buttons = [
        InlineKeyboardButton(text="Games Base Information", callback_data="g_b_i")
    ]

    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)

    await edit_message("Hello, I'm your informant, what do you want to know?", reply_markup=keyboard)
