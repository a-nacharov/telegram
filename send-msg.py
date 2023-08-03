#import asyncio
from telethon import TelegramClient

# Remember to use your own values from my.telegram.org!
api_id = 29115625
api_hash = '273233a134705d12fadc24de9f4048e9'
client = TelegramClient('nacharov', api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()

    username = me.username

    for i in range(20):
        await client.send_message('ace-group', 'Laze muce - ' + str(i))

with client:
    client.loop.run_until_complete(main())
