# Telegram Bot with SQLite Logging

This project is a Telegram bot that logs user actions to an SQLite database and returns the number of interactions. The main goal of this project is to test how Docker works using a Telegram bot example with a separate SQLite database from `data`-folder and environment variable from `.env`.

## Docker Setup

1. Make image based on `Dockerfile`:
    ```sh
    docker build -t hello-docker-bot:latest .
    ```

2. Run container:
    ```sh
    docker run -d `
    -v "${PWD}\data:/app/data" `
    --env-file .\.env `
    --name hello-docker-bot_container `
    hello-docker-bot:latest
    ```

3. Stop container:
    ```sh
    docker stop hello-docker-bot_container
    ```

## Run from .venv

1. Add variable:
    ```sh
    $env:TELEGRAM_TOKEN = "XXX"
    ```

2. Run `bot.py`

## Usage

Send the `/start` command to your Telegram bot. The bot will respond with the system type and the number of interactions.