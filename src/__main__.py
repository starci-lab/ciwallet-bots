#imports
import constants as constants
from services.telegram_bot.bot import Bot

def callback(ch, method, properties, body):
    print(f"Received {body}")

def main():
    bot = Bot(constants.TELEGRAM_API_TOKEN)
    bot.run()

if __name__ == "__main__":
    main() 