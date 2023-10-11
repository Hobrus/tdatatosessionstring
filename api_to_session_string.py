from telethon.sessions import StringSession
from telethon.sync import TelegramClient

api_id = 23049196 # Замените на ваш API ID
api_hash = '1b7bb0d68f84898b4c2c008500ad4b21'  # Замените на ваш API Hash

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())
