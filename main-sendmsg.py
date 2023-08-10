import checkchannelgroup
import sendmsggroup
import sendmsgchannel
import asyncio


if __name__ == '__main__':
    with open('file.txt') as reader:
        line = reader.readline()
        while line != '': 
            #proverka na tip na chat
            #dali e group ili channel
            chat_type = asyncio.run(checkchannelgroup.main(line.strip()))
            
            #ako e group
            #prati poraka za group
            if chat_type == "group":
                asyncio.run(sendmsggroup.main(line.strip(), "poraka"))
            
            #ako e channel
            #prati poraka za channel
            if chat_type == "channel":
                asyncio.run(sendmsgchannel.main(line.strip(), "Nice"))

            line = reader.readline()
