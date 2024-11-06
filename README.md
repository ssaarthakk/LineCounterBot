# Line Counter Bot

This is a simple Telegram bot written in Python that counts the number of lines in a message. You can send any message to the bot, and it will respond with the line count.

## Requirements

- Python 3.8 or later
- `python-telegram-bot` library

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/line-counter-bot.git
cd line-counter-bot
```

### 2. Install Dependencies

It's recommended to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Get a Telegram Bot Token

1. Open Telegram and search for [BotFather](https://t.me/BotFather).
2. Start a chat with BotFather and use the `/newbot` command to create a new bot.
3. Follow the instructions to get your bot token.

### 4. Set Up Environment Variables

Create a `.env` file in the project root and add your Telegram bot token:

```plaintext
TELEGRAM_TOKEN=your_bot_token_here
```

### 5. Run the Bot

To start the bot, run the following command:

```bash
python bot.py
```

Your bot should now be running and ready to use!
