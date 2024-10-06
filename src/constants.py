import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables
TELEGRAM_API_TOKEN = os.environ.get("TELEGRAM_API_TOKEN", "")
TELEGRAM_MINIAPP_URL = os.environ.get("TELEGRAM_MINIAPP_URL", "https://3000.starci.net")

KAFKA_1_HOST = os.environ.get("KAFKA_1_HOST", "localhost")
KAFKA_1_PORT = int(os.environ.get("KAFKA_1_PORT", "29092")) 

# Brokers
INVITE_GROUP_TOPIC = "invite"

# Default values
DEFAULT_KEY = "defaultKey"
DEFAULT_GROUP_ID = "defaultGroupId"