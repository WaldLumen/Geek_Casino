# dices
from asyncio import sleep

from aiogram import types

import logging

from tgbot.bot.Banque import Banque

logging.getLogger("psycopg").setLevel(logging.DEBUG)

bank = Banque()


async def start_cubes(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Throw", callback_data="throw"))
    keyboard.add(types.InlineKeyboardButton(text=" ⬅ Menu ⬅", callback_data="games"))
    await call.message.edit_text("Throw Dices:", reply_markup=keyboard)


async def throw_dice(call: types.CallbackQuery):
    user_id = call.from_user.id

    bank.start_transaction()
    bank.select_cash_for_update(user_id)

    cash = bank.show_cash(user_id)

    if cash < 300:

        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text=" ⬅ Menu ⬅", callback_data="to_menu"))
        await call.message.edit_text("There are not enough shekels on your account. ", reply_markup=keyboard)

    else:

        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text=" ⬅Menu⬅", callback_data="games"),
                     types.InlineKeyboardButton(text="🔄Play Again🔄", callback_data="dices"))

        await call.message.edit_text("Throwing Dices:")

        await call.message.answer("You:")
        usr = await call.message.answer_dice()

        await call.message.answer("Bot:")
        bott = await call.message.answer_dice()

        await sleep(3)

        if bott.dice.value > usr.dice.value:
            await call.message.answer("You lose;\n"
                                      "300₪ was deducted from your account", reply_markup=keyboard)

            bank.cash_withdrawal(300, user_id)

        elif bott.dice.value < usr.dice.value:
            await call.message.answer("You Win;\n"
                                      "300₪ was credited to your balance", reply_markup=keyboard)
            bank.replenishment(300, user_id)

        elif bott.dice.value == usr.dice.value:
            await call.message.answer("Draw", reply_markup=keyboard)
            bank.commit_transaction()
