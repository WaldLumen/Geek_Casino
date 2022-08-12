import logging
from os import getenv

from aiogram import Bot, Dispatcher, executor

from menu.main_menu import main_menu
from on_startup import on_startup
from tgbot.bot.games.colors.big import start_game_big, send_random_words_big, colorr_big, color_factory_big

from tgbot.bot.games.colors.classic \
    import start_game_classic, color_factory_classic, colorr_classic, send_random_words_classic
from tgbot.bot.games.colors.duo import start_game_duo, colorr_duo, send_random_words_duo, color_factory_duo
from tgbot.bot.games.colors.giant import send_random_words_giant, colorr_giant, color_factory_giant, start_game_giant

from tgbot.bot.menu.colors_menu import colors_menu

from tgbot.bot.games.dices.dices import start_cubes, throw_dice

from tgbot.bot.menu.games import menu_games
from tgbot.bot.menu.help import help_menu, games_base_information
from tgbot.bot.menu.profile import profile
from tgbot.bot.menu.to_menu import to_main_menu, to_help_menu

bot = Bot(getenv(str("token")))
dp = Dispatcher(bot)

logging.basicConfig(level=logging.ERROR)


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
    dp.register_callback_query_handler(throw_dice, text="throw")


def colors_duo():
    dp.register_callback_query_handler(colors_menu, text='colors_menu')
    dp.register_callback_query_handler(start_game_duo, text='duo')
    dp.register_callback_query_handler(send_random_words_duo, text='random_value')
    dp.register_callback_query_handler(colorr_duo, color_factory_duo.filter())


def colors_classic():
    dp.register_callback_query_handler(start_game_classic, text='classic')
    dp.register_callback_query_handler(send_random_words_classic, text='random_value')
    dp.register_callback_query_handler(colorr_classic, color_factory_classic.filter())


def colors_big():
    dp.register_callback_query_handler(start_game_big, text='big')
    dp.register_callback_query_handler(send_random_words_big, text='random_value')
    dp.register_callback_query_handler(colorr_big, color_factory_big.filter())


def colors_giant():
    dp.register_callback_query_handler(start_game_giant, text='giant')
    dp.register_callback_query_handler(send_random_words_giant, text='random_value')
    dp.register_callback_query_handler(colorr_giant, color_factory_giant.filter())


reg_main_commands()
help_commands()
to_menu()
dices()

colors_duo()
colors_classic()
colors_big()
colors_giant()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
