# dices
from asyncio import sleep

from aiogram import types

from tgbot.bot.Dwarf import Dwarf


async def start_cubes(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Throw", callback_data="throw"))
    keyboard.add(types.InlineKeyboardButton(text=" ⬅ Menu ⬅", callback_data="to_menu"))
    await call.message.edit_text("Throw Dices:", reply_markup=keyboard)


async def throw(call: types.CallbackQuery):
    elf = Dwarf()

    user_id = call.from_user.id
    cash = elf.dices(user_id)

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton(text=" ⬅Menu⬅", callback_data="to_menu"),
                 types.InlineKeyboardButton(text="🔄Play Again🔄", callback_data="dices"))

    if cash > 300:
        await call.message.edit_text("Throwing Dices:")

        await call.message.answer("You:")
        usr = await call.message.answer_dice()

        await call.message.answer("Bot:")
        bott = await call.message.answer_dice()

        await sleep(4)

        await call.message.delete()

        if bott.dice.value > usr.dice.value:
            await call.message.answer("You lose;\n"
                                      "300₪ was deducted from your account", reply_markup=keyboard)
            elf.cash_withdrawal(ball=300, user_id=user_id)
        elif bott.dice.value < usr.dice.value:
            await call.message.answer("You Win;\n"
                                      "300₪ was credited to your balance", reply_markup=keyboard)
            elf.replenishment(ball=300, user_id=user_id)
        else:
            await call.message.answer("Draw", reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text=" ⬅ Menu ⬅", callback_data="to_menu"))
        await call.message.edit_text("There are not enough shekels on your account", reply_markup=keyboard)
