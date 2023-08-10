import os
import sys
import asyncio

from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import FloodWaitError
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client_name = os.getenv('CLIENT_NAME')

async def main(channel , message):
    async with TelegramClient(client_name, api_id, api_hash) as client:
        try:
            await client.send_message(channel, message)
            await asyncio.sleep(delay=2)
        except FloodWaitError as fwe:
            print(f'Waiting for {fwe}')
            await asyncio.sleep(delay=2)
        except Exception as err:
            print(f"Encountered an error while sending message {channel}\n{err}")
