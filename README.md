# All_language_translator_telegram

This is a simple Telegram bot that translates text into multiple languages using the Google Translate API. It's implemented in Python.

## Dependencies

- `telepot`: A Python framework for Telegram Bot API.
- `googletrans`: A free and unlimited python library that implemented Google Translate API.

## Setup

1. Install the dependencies:

```bash
pip install googletrans==3.1.0a0
pip install telepot

Get your bot token from BotFather.

Replace the BOT_TOKEN and ADMIN_ID_NUMBER in the translator.py script with your bot token and admin ID.

If you’re behind a proxy, replace the proxy_url with your proxy server.

Usage
Run the script:

python translator.py

The bot will now be online and ready to translate text into multiple languages.

Commands
/start: The bot will send a welcome message.
/change: (Admin only) Change the welcome message.
Note
This bot uses a list of languages from the googletrans library. It translates the input text into all these languages and sends the result back.

How to get user id
You can get your user ID from here.

Libraries used in this code
googletrans 3.1.0a0
telepot
