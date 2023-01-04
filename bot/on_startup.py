# reg commands for fast access
# creating database
import logging
from os import getenv

from aiogram import types, Bot, Dispatcher

from bot.Banque import Banque

bot = Bot(getenv("token"))
dp = Dispatcher(bot)
database = Banque()


async def on_startup(dp):
    database.create_table()

    commands = [
        types.BotCommand(command="start", description='-bot navigation'),
        types.BotCommand(command="help", description='-start/reboot bot')
    ]

    await bot.set_my_commands(commands)
