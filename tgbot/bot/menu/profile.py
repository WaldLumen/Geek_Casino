# profile
import psycopg
from aiogram import types


async def profile(call: types.CallbackQuery):
    user_id = call.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text=" ⬅ Menu ⬅", callback_data="to_menu"))

    with psycopg.connect("dbname=casinobot user=postgres") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT cash FROM users WHERE id = '%s'" % user_id)

            await call.message.edit_text(f"id card: <b>%d</b>\n"
                                         f"Balance: <b>%s ₪</b>" % (user_id, cur.fetchone()[0]),
                                         reply_markup=keyboard,
                                         parse_mode='HTML')

