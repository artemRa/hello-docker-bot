# Telegram Bot with SQLite Logging

This project is a Telegram bot that logs user actions to an SQLite database and returns the number of interactions.

## Setup and Run

### Local Setup

1. Clone the repository:
    ```sh
    git clone <your-repo-url>
    cd <repo-name>
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `config.json` file with your Telegram token:
    ```json
    {
        "TOKEN": "your_telegram_token"
    }
    ```

4. Initialize the database:
    ```sh
    python db_init.py
    ```

5. Run the bot:
    ```sh
    python bot.py
    ```

### Docker Setup

1. Build the Docker image:
    ```sh
    docker build -t telegram-bot .
    ```

2. Run the container with a volume for the database:
    ```sh
    docker run -d --name telegram-bot -v data:/app/data telegram-bot
    ```

## Usage

Send the `/start` command to your Telegram bot. The bot will respond with the system type and the number of interactions.