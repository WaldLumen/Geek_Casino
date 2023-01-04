from aiogram import types

from bot.Banque import Banque

database = Banque()


async def on_startup(bot):
    database.create_table()

    commands = [
        types.BotCommand(command="start", description='-bot navigation'),
        types.BotCommand(command="help", description='-start/reboot bot')
    ]

    await bot.set_my_commands(commands)
