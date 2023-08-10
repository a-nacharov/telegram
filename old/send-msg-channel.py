import os
import sys

from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client_name = os.getenv('CLIENT_NAME')
client = TelegramClient(client_name, api_id, api_hash)

channel = sys.argv[1]
msg = sys.argv[2]

async def main():
    
    # channel_username = 'https://t.me/GrahamAllen1'
    #channel_username = 'https://t.me/nacharov_channel'
    for message in await client.get_messages(channel, limit=1):
        await client.send_message(entity=message.peer_id.channel_id, message=msg,comment_to=message.id)

with client:
    client.loop.run_until_complete(main())
