import os

def printFile(path):
    content =""
    file = open(path, "r")
    for line in file:
        content += line
    return content

path = input()

if os.path.isfile(path):
    content = printFile(path)
    print(path + "=", content)
elif os.isdir(path):

    for file in os.listdir(path):
        if os.path.isfile(path):
            content = printFile(path)
            print(path + "=", content)
        elif os.isdir(os.path.join(path, file)):
            print(file +":", os.path.join(path,file))


