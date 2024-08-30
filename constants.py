#imports
import os
from dotenv import load_dotenv

#configurations
load_dotenv()
 
telegram_api_token = os.environ.get("TELEGRAM_API_TOKEN")