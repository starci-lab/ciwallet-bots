
import logging
import sys
from services.database.repositories.users import UsersRepository
from config import env
from telegram import InlineKeyboardButton, Update, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ContextTypes, MessageHandler, filters

class Bot:
    def __init__(self):
        self.application = ApplicationBuilder().token(env.TELEGRAM_CIFARM_API_TOKEN).build()
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)],
        )
        #init new instance
        self.users_repository = UsersRepository()

        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Cifarm Token: {env.TELEGRAM_CIFARM_API_TOKEN}")
    
    async def handle_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        photo_path = "assets/cifarm-background.png"
        keyboard = [[InlineKeyboardButton("Play Cifarm", 
                    web_app=WebAppInfo(env.TELEGRAM_CIFARM_MINIAPP_URL))]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        chat = update.effective_chat
        count = self.users_repository.count()

        if chat: 
            await context.bot.send_photo(
                chat_id=chat.id,
                photo=open(photo_path, "rb"),
                caption="""🌾 Cifarm: Farm-to-earn on Telegram! 🌾
Step into the first multichain farming game on Telegram, powered by Ciwallet and Wormhole. Farm, help, visit, and even steal from other players while earning airdropped tokens! 💰

🚀 Free to play & packed with rewards! Unlock the potential of multichain gaming with Cifarm. 🌱✨
👉 Start playing now and grow your farm!
👩‍🌾 Total farmers: {count}""".format(count=count),
                reply_markup=reply_markup
            )
 
    def run(self):
        start_handler = CommandHandler("start", self.handle_start) 
        self.application.add_handler(start_handler)
        self.application.run_polling()
