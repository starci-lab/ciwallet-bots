
import logging
import sys

from config import env
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

class Bot:
    def __init__(self):
        self.application = ApplicationBuilder().token(env.TELEGRAM_CIWALLET_API_TOKEN).build()

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)],
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Ciwallet Token: {env.TELEGRAM_CIWALLET_API_TOKEN}")
    
    async def handle_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        photo_path = "assets/background.jpg"
        keyboard = [[InlineKeyboardButton("Open Ciwallet", web_app=WebAppInfo(env.TELEGRAM_CIWALLET_MINIAPP_URL))]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        chat = update.effective_chat
        if chat: 
            await context.bot.send_photo(
                chat_id=chat.id,
                photo=open(photo_path, "rb"),
                caption="""🎉 Introducing Ci Wallet — a Telegram-based cross-chain wallet that transforms cryptocurrency management by enabling you to send, receive, and swap assets across multiple blockchains directly within your Telegram app. With Ci Wallet, you can effortlessly handle a diverse range of cryptocurrencies in a familiar chat environment, making cross-chain transactions simpler and more secure than ever before.""",
                reply_markup=reply_markup
            )  
        
    def run(self):
        start_handler = CommandHandler("start", self.handle_start)  
        self.application.add_handler(start_handler)
        self.application.run_polling()
