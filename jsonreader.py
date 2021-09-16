import json

file=open('tigergarden.json','r')

b=json.load(file)
print(b)

file.close()