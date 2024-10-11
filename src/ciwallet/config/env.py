import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

print(os.environ)

# Environment variables
TELEGRAM_CIWALLET_API_TOKEN = os.environ.get("TELEGRAM_CIWALLET_API_TOKEN", "")
TELEGRAM_CIWALLET_MINIAPP_URL = os.environ.get("TELEGRAM_CIWALLET_MINIAPP_URL", "https://3000.starci.net")