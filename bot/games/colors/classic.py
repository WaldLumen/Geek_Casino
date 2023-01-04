import random
from asyncio import sleep

from aiogram import types
from aiogram.utils.callback_data import CallbackData

from bot.Banque import Banque

color_factory_classic = CallbackData("cl_classic", "color_classic")

colors = ['White', 'Black', 'Red']


async def start_game_classic(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    for color in colors:
        keyboard.add(types.InlineKeyboardButton(text=color, callback_data=color_factory_classic.new(color_classic=color)))
    keyboard.add(types.InlineKeyboardButton(text=" ⬅ Menu ⬅", callback_data="colors_menu"))

    await call.message.edit_text("Choice Color: ", reply_markup=keyboard)


async def send_random_words_classic(call: types.CallbackQuery):
    choice = random.choice(colors)

    await call.message.answer(str(choice))


async def colorr_classic(call: types.CallbackQuery, callback_data: dict):
    bank = Banque()

    user_id = call.from_user.id

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton(text=" ⬅Menu⬅", callback_data="games"),
                 types.InlineKeyboardButton(text="🔄Play Again🔄", callback_data="classic"))

    bank.start_transaction()
    bank.select_cash_for_update(user_id)

    if bank.show_cash(user_id) < 300:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text=" ⬅ Menu ⬅", callback_data="to_menu"))
        await call.message.edit_text("There are not enough shekels on your account", reply_markup=keyboard)

    else:
        await call.message.edit_text("Choice Color: ")
        color = callback_data.get('color_classic')
        true_color = random.choice(colors)

        await sleep(2)

        await call.message.answer(f"Your color is - {color}")

        if color == true_color:
            await call.message.answer(f"You Win;\n"
                                      f"400₪ was credited to your balance", reply_markup=keyboard)
            bank.replenishment(ball=400, user_id=user_id)
        else:
            await call.message.answer(f"You Lose;\n"
                                      f"300₪ was deducted from your account", reply_markup=keyboard)
            bank.cash_withdrawal(ball=300, user_id=user_id)
        bank.commit_transaction()
