from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


from bot.Banque import Banque


async def profile(call: CallbackQuery):
    bank = Banque()

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="⬅ Menu ⬅", callback_data="to_menu"))

    cash = bank.show_cash(call.from_user.id)

    await call.message.edit_text('<b>Id</b>: %d\n'
                                 '<b>Balance</b>: %s ₪' % (call.from_user.id, cash),

                                 reply_markup=keyboard,
                                 parse_mode='HTML')
