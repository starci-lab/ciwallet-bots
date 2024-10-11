ARG PYTHON_VERSION=3.12.2
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /app

RUN pip install python-telegram-bot
RUN pip install python-dotenv
RUN pip install sqlalchemy

COPY . .
EXPOSE 9992
RUN python3 src/ciwallet/__main__.py