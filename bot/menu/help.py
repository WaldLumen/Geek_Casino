# help
from os import getenv

from aiogram import Bot, Dispatcher, types

bot = Bot(getenv(str("token")))
dp = Dispatcher(bot)


async def help_menu(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Games Base Information", callback_data="g_b_i")
    ]

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)

    await message.answer("Hello, I'm your informant, what do you want to know?", reply_markup=keyboard)


async def games_base_information(call: types.CallbackQuery):
    buttons = [
        types.InlineKeyboardButton(text="To Menu", callback_data="help_menu")
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
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await call.message.edit_text(text, reply_markup=keyboard)



