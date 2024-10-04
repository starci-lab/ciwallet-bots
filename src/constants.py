#imports
import os
from dotenv import load_dotenv

#configurations
load_dotenv()
 
telegram_api_token = os.environ.get("TELEGRAM_API_TOKEN")
telegram_miniapp_url = os.environ.get("TELEGRAM_MINIAPP_URL") or "https://3000.starci.net"
print(telegram_miniapp_url)