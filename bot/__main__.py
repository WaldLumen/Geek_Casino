import logging
from os import getenv

from aiogram import Bot, Dispatcher, executor

from reg_all_commands import reg_commands
from on_startup import on_startup

# A few necessary variables
bot = Bot(getenv(str("token")))
dp = Dispatcher(bot)

# logging
logging.basicConfig(level=logging.ERROR)


# Register all the commands and callbacks that we use
reg_commands(dp)

# Register some actions that are necessary for normal operation of bot
on_startup(bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
