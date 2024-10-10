from services.telegram_bot.bot import Bot
import env as env

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()