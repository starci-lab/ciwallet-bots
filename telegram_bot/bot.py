
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

class Bot:
    def __init__(self, token):
        self.application = ApplicationBuilder().token(token).build()
    
    async def handle_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        photo_path = "assets/background.jpg"
        keyboard = [[InlineKeyboardButton("Open Ci Wallet", web_app=WebAppInfo("https://ciwallet.starci.net"))]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_photo(
            chat_id=update.effective_chat.id, 
            photo=open(photo_path, "rb"),
            caption="""🎉 Introducing Ci Wallet — a Telegram-based cross-chain wallet that transforms cryptocurrency management by enabling you to send, receive, and swap assets across multiple blockchains directly within your Telegram app. With Ci Wallet, you can effortlessly handle a diverse range of cryptocurrencies in a familiar chat environment, making cross-chain transactions simpler and more secure than ever before.""",
            reply_markup=reply_markup
        )
        
    def run(self):
        start_handler = CommandHandler('start', self.handle_start)  
        self.application.add_handler(start_handler)
        self.application.run_polling()
