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

    channel = await client.get_entity('ace-group')
    messages = await client.get_messages(channel, limit= None) #pass your own args

    #then if you want to get all the messages text
    for x in messages:
        if(x.from_id.user_id == me.id):
#            print(x.message)
            await client.delete_messages(channel, message_ids=x.id)

        #print(x.id) #return message.text

with client:
    client.loop.run_until_complete(main())
