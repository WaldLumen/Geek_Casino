# profile

from aiogram import types

from tgbot.bot.Banque import Banque


async def profile(call: types.CallbackQuery):
    bank = Banque()

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text=" ⬅ Menu ⬅", callback_data="to_menu"))

    cash = bank.show_cash(user_id=call.from_user.id)

    await call.message.edit_text('Id card: <b>%d</b>\n'
                                 'Balance: <b>%s ₪</b>' % (call.from_user.id, cash),
                                 reply_markup=keyboard,
                                 parse_mode='HTML')
