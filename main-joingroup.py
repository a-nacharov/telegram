import joingroupchannel
import asyncio


if __name__ == '__main__':
    with open('file.txt') as reader:
        line = reader.readline()
        while line != '': 
            
            asyncio.run(joingroupchannel.main(line.strip()))
            
            line = reader.readline()

