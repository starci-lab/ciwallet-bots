#imports
import constants
from telegram_bot.bot import Bot

def main():
    print(constants.telegram_api_token)
    bot = Bot(constants.telegram_api_token)
    bot.run()

if __name__ == "__main__":
    main() 