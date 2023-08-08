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
message = sys.argv[2]

# print(message)
async def main():
    
    await client.send_message(group, message)

with client:
    client.loop.run_until_complete(main())
