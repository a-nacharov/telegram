array = []
with open('file.txt') as reader:
    line = reader.readline()
    while line != '': 
        array.append(line.strip())
        line = reader.readline()
print(array)
