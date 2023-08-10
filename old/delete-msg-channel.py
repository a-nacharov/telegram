import os
import sys

from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client_name = os.getenv('CLIENT_NAME')
client = TelegramClient(client_name, api_id, api_hash)

group = sys.argv[1]
limits = sys.argv[2]

async def main():

    me = await client.get_me()

    channel = await client.get_entity(group)
    messages = await client.get_messages(channel, limit= int(limits)) #pass your own args

    for x in messages:
        
        await client.delete_messages(channel, message_ids=x.id)

with client:
    client.loop.run_until_complete(main())
