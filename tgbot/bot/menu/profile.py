# profile

from aiogram import types

from tgbot.bot.Dwarf import Dwarf

elf = Dwarf()


async def profile(call: types.CallbackQuery):

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text=" ⬅ Menu ⬅", callback_data="to_menu"))

    cash = elf.profile(user_id=call.from_user.id)

    await call.message.edit_text('id card: <b>%d</b>\n'
                                 'Balance: <b>%s ₪</b>' % (call.from_user.id, cash[0]),
                                 reply_markup=keyboard,
                                 parse_mode='HTML')
