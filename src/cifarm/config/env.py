# Description: Environment variables for the project

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables
TELEGRAM_CIFARM_API_TOKEN = os.environ.get("TELEGRAM_CIFARM_API_TOKEN", "")
TELEGRAM_CIFARM_MINIAPP_URL = os.environ.get("TELEGRAM_CIFARM_MINIAPP_URL", "")

# Postgres
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "host.docker.internal")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5433")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "cifarm")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "")
