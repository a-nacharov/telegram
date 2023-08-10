import os
import sys
import asyncio

from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client_name = os.getenv('CLIENT_NAME')

async def main(group):
    async with TelegramClient(client_name, api_id, api_hash) as client:

        channel = await client.get_entity(group)

        if channel.broadcast==True:
            return ("channel")
        else:
            return ("group")
