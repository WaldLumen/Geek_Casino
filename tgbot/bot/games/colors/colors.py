import random
from asyncio import sleep

from aiogram import types
from aiogram.utils.callback_data import CallbackData

from tgbot.bot.Dwarf import Dwarf

color_factory = CallbackData("cl", "color")

colors = ['White', 'Black', 'Gray']


async def start_game(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    for color in colors:
        keyboard.add(types.InlineKeyboardButton(text=color, callback_data=color_factory.new(color=color)))
    keyboard.add(types.InlineKeyboardButton(text=" ⬅ Menu ⬅", callback_data="to_menu"))

    await call.message.edit_text("Choice Color: ", reply_markup=keyboard)


#
async def send_random_words(call: types.CallbackQuery):
    choice = random.choice(colors)

    await call.message.answer(str(choice))


#
async def colorr(call: types.CallbackQuery, callback_data: dict):
    elf = Dwarf()

    user_id = call.from_user.id
    cash = elf.dices(user_id)

    if cash > 300:
        await call.message.edit_text("Choice Color: ")
        color = callback_data.get('color')
        true_color = random.choice(colors)

        await sleep(4)

        if color == true_color:
            await call.message.answer(f"You Win;\n"
                                      f"300₪ was credited to your balance", reply_markup=keyboard3)
            elf.replenishment(ball=300, user_id=user_id)
        else:
            await call.message.answer(f"You Lose;\n"
                                      f"300₪ was deducted from your account", reply_markup=keyboard3)
            elf.cash_withdrawal(ball=300, user_id=user_id)
    else:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text=" ⬅ Menu ⬅", callback_data="to_menu"))
        await call.message.edit_text("There are not enough shekels on your account", reply_markup=keyboard)
