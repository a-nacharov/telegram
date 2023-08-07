import os

from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client_name = os.getenv('CLIENT_NAME')
client = TelegramClient(client_name, api_id, api_hash)

async def main():
    # 
    # me = await client.get_me()
    # 
    # username = me.username

    for i in range(20):
        await client.send_message('https://t.me/testeramn', 'marcelo - ' + str(i))

with client:
    client.loop.run_until_complete(main())
