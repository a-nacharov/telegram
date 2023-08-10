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

async def main(channel , msg):
    async with TelegramClient(client_name, api_id, api_hash) as client:
        try:
            for message in await client.get_messages(channel, limit=1):
                await client.send_message(entity=message.peer_id.channel_id, message=msg,comment_to=message.id)
            await asyncio.sleep(delay=2)
        except FloodWaitError as fwe:
            print(f'Waiting for {fwe}')
            await asyncio.sleep(delay=2)
        except Exception as err:
            print(f"Encountered an error while sending message {channel}\n{err}")
