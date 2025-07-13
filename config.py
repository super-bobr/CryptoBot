import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN") #тут он берет токен
DEFAULT_CRYPTOS = os.getenv("DEFAULT_CRYPTOS", "").split(",") #и читает какую крипту берем
