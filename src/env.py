# Description: Environment variables for the project

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables
TELEGRAM_CIWALLET_API_TOKEN = os.environ.get("TELEGRAM_CIWALLET_API_TOKEN", "")
TELEGRAM_CIWALLET_MINIAPP_URL = os.environ.get("TELEGRAM_CIWALLET_MINIAPP_URL", "")

# Environment variables
TELEGRAM_CIFARM_API_TOKEN = os.environ.get("TELEGRAM_CIFARM_API_TOKEN", "")
TELEGRAM_CIFARM_MINIAPP_URL = os.environ.get("TELEGRAM_CIFARM_MINIAPP_URL", "")

# Postgres
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "")
