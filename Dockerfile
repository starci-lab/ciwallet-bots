ARG PYTHON_VERSION=3.12.2
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /app

RUN pip install python-telegram-bot
RUN pip install python-dotenv

COPY . .

EXPOSE 9992
CMD python3 \src\__main__.py
