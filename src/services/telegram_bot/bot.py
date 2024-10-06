
import logging
from os import error
import sys
import uuid
import constants
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from services.clients.kafka import KafkaClient

class Bot:
    def __init__(self, token):
        self.application = ApplicationBuilder().token(token).build()
        self.kafka_client = KafkaClient()
        self.producer_key = uuid.uuid4().__str__()
        self.kafka_client.createProducer(self.producer_key)

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)],
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Token: {token}")
    
    async def handle_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            photo_path = "assets/background.jpg"
            keyboard = [[InlineKeyboardButton("Open Ci Wallet", web_app=WebAppInfo(constants.TELEGRAM_MINIAPP_URL))]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            if not context._user_id: raise Exception("User id not found")
            if not context.args: raise Exception("Args id not found")
            
            if (context.args.__len__() > 0): 
                data = {
                    "user_id": context._user_id,
                    "origin_user_id": context.args[0]
                }
                self.kafka_client.produce(
                    self.producer_key, 
                    constants.INVITE_GROUP_TOPIC, 
                    data.__str__())

            chat = update.effective_chat
            if chat: 
                await context.bot.send_photo(
                    chat_id=chat.id,
                    photo=open(photo_path, "rb"),
                    caption="""🎉 Introducing Ci Wallet — a Telegram-based cross-chain wallet that transforms cryptocurrency management by enabling you to send, receive, and swap assets across multiple blockchains directly within your Telegram app. With Ci Wallet, you can effortlessly handle a diverse range of cryptocurrencies in a familiar chat environment, making cross-chain transactions simpler and more secure than ever before.""",
                    reply_markup=reply_markup
                )  
        except Exception as e:
            self.logger.error(f"Exception found: {e}") 
        
    def run(self):
        start_handler = CommandHandler("start", self.handle_start)  
        self.application.add_handler(start_handler)
        self.application.run_polling()
