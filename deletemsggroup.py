import os
import sys
import asyncio

from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client_name = os.getenv('CLIENT_NAME')
client = TelegramClient(client_name, api_id, api_hash)

async def main(group):
    async with TelegramClient(client_name, api_id, api_hash) as client:
        try:
            me = await client.get_me()
            for message in await client.get_messages(group, limit=1):
                if(message.from_id!=None):
                    if(message.from_id.user_id == me.id):
                        await client.delete_messages(group, message_ids=message.id)
            await asyncio.sleep(delay=2)
        except FloodWaitError as fwe:
            print(f'Waiting for {fwe}')
            await asyncio.sleep(delay=2)
        except Exception as err:
            print(f"Encountered an error while sending message {group}\n{err}")
