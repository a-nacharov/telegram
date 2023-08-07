import os

from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client_name = os.getenv('CLIENT_NAME')
client = TelegramClient(client_name, api_id, api_hash)

async def main():

    me = await client.get_me()

    channel = await client.get_entity('https://t.me/testeramn')
    messages = await client.get_messages(channel, limit= 20) #pass your own args

    for x in messages:
        if(x.from_id.user_id == me.id):
            # print(x.message)
            await client.delete_messages(channel, message_ids=x.id)

        #print(x.id) #return message.text

with client:
    client.loop.run_until_complete(main())
