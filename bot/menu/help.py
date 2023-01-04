from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message


async def help_menu(message: Message):
    buttons = [
        InlineKeyboardButton(text="Games Base Information", callback_data="g_b_i")
    ]

    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)

    await message.answer("Hello, I'm your informant, what do you want to know?", reply_markup=keyboard)


async def games_base_information(edit_message: CallbackQuery.message.edit_text):
    buttons = [
        InlineKeyboardButton(text="To Menu", callback_data="help_menu")
    ]
    text = '''
Brief information about the game and the bot itself:
1. Cost of one game in one of the modes (dices, colors) - 200 shekels.
If you win, you will receive 400 shekels, if you lose, you will be credited with 0 shekels.
2. Cost of one game in the modes: slots, lottery, is 100 shekels, and the winnings
depend on the combination of numbers
/ symbols
\n
Bot author: @Syllvvia.
\n
Thank you, @paadoru, for the tips on building a bot
            '''
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await edit_message(text, reply_markup=keyboard)
