from os import getenv

from dotenv import load_dotenv
load_dotenv()


class BotEnv:
    BOT_TOKEN = getenv('BOT_TOKEN')


class Env:
    bot = BotEnv()
