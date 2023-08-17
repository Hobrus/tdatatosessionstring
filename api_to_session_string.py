from telethon.sessions import StringSession
from telethon.sync import TelegramClient

api_id = 111 # Замените на ваш API ID
api_hash = '111'  # Замените на ваш API Hash

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())
