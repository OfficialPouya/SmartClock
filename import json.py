import json

# read file
with open('city.list.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

# show values
print("Name: " + str(obj['name']))
