# profile

from aiogram import types

from tgbot.bot.Banque import Banque


async def profile(call: types.CallbackQuery):
    bank = Banque()

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="⬅ Menu ⬅", callback_data="to_menu"))

    cash = bank.show_cash(call.from_user.id)

    await call.message.edit_text('<b>Id</b>: %d\n'
                                 '<b>Balance</b>: %s ₪' % (call.from_user.id, cash),

                                 reply_markup=keyboard,
                                 parse_mode='HTML')
