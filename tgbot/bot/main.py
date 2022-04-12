import logging
from os import getenv

from aiogram import Bot, Dispatcher, executor

from menu.main_menu import main_menu
from set_commands import on_startup
from tgbot.bot.menu.games import menu_games
from tgbot.bot.menu.help import help_menu, games_base_information
from tgbot.bot.menu.profile import profile
from tgbot.bot.menu.to_menu import to_main_menu, to_help_menu

bot = Bot(getenv(str("token")))
dp = Dispatcher(bot)


logging.basicConfig(level=logging.INFO)


def reg_main_coms():
    dp.register_message_handler(main_menu, commands="start")
    dp.register_callback_query_handler(profile, text="profile")
    dp.register_callback_query_handler(menu_games, text="games")


def help():
    dp.register_message_handler(help_menu, commands="help")
    dp.register_callback_query_handler(games_base_information, text="g_b_i")


def to_menu():
    dp.register_callback_query_handler(to_main_menu, text="to_menu")
    dp.register_callback_query_handler(to_help_menu, text="help_menu")




reg_main_coms()
help()
to_menu()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
