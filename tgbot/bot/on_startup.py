# reg commands for fast access
import logging
from os import getenv

from aiogram import types, Bot, Dispatcher

from tgbot.bot.Dwarf import Dwarf

bot = Bot(getenv("token"))
dp = Dispatcher(bot)
elf = Dwarf()


async def on_startup(dp):
    elf.create_table()
    logging.info('bot has been launched')

    help_text = '-bot navigation'
    start_text = '-start/reboot bot'
    commands = [
        types.BotCommand(command="start", description=start_text),
        types.BotCommand(command="help", description=help_text)
    ]
    await bot.set_my_commands(commands)
