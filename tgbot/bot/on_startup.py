# reg commands for fast access
import logging
from os import getenv

from aiogram import types, Bot, Dispatcher

from tgbot.bot.Banque import Banque

bot = Bot(getenv("token"))
dp = Dispatcher(bot)
database = Banque()


async def on_startup(dp):
    database.create_table()
    help_text = '-bot navigation'
    start_text = '-start/reboot bot'
    commands = [
        types.BotCommand(command="start", description=start_text),
        types.BotCommand(command="help", description=help_text)
    ]
    await bot.set_my_commands(commands)
