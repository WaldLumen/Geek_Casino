import logging
from os import getenv

from aiogram import Bot, Dispatcher, executor

from menu.main_menu import main_menu
from on_startup import on_startup

from tgbot.bot.menu.colors_menu import color_menu
from tgbot.bot.games.colors.classic import send_random_words, colorr, color_factory, start_game_classic
from tgbot.bot.games.colors.duo import send_random_words, colorr, color_factory, start_game_duo
from tgbot.bot.games.colors.giant import send_random_words, colorr, color_factory, start_game_giant
from tgbot.bot.games.colors.big import send_random_words, colorr, color_factory, start_game_big

from tgbot.bot.games.dices.dices import start_cubes, throw

from tgbot.bot.menu.games import menu_games
from tgbot.bot.menu.help import help_menu, games_base_information
from tgbot.bot.menu.profile import profile
from tgbot.bot.menu.to_menu import to_main_menu, to_help_menu

bot = Bot(getenv(str("token")))
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


def reg_main_commands():
    dp.register_message_handler(main_menu, commands="start")
    dp.register_callback_query_handler(profile, text="profile")


def help_commands():
    dp.register_message_handler(help_menu, commands="help")
    dp.register_callback_query_handler(games_base_information, text="g_b_i")


def to_menu():
    dp.register_callback_query_handler(to_main_menu, text="to_menu")
    dp.register_callback_query_handler(to_help_menu, text="help_menu")
    dp.register_callback_query_handler(menu_games, text="games")


def dices():
    dp.register_callback_query_handler(start_cubes, text="dices")
    dp.register_callback_query_handler(throw, text="throw")


def colors():
    dp.register_callback_query_handler(color_menu, text='colors_menu')

    dp.register_callback_query_handler(start_game_big, text='big')
    dp.register_callback_query_handler(start_game_classic, text='classic')
    dp.register_callback_query_handler(start_game_duo, text='duo')
    dp.register_callback_query_handler(start_game_giant, text='giant')

    dp.register_callback_query_handler(send_random_words, text='random_value')
    dp.register_callback_query_handler(colorr, color_factory.filter())


reg_main_commands()
help_commands()
to_menu()
dices()
colors()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
