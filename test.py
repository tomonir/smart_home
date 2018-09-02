import json

data = [{'time':'20:04','transport':'S5','direction':'bietigheim-bissingen'},{'time':'20:14','transport':'S4','direction':'backnang'},{'time':'20:34','transport':'S5','direction':'bietigheim-bissingen'},{'time':'21:04','transport':'S5','direction':'bietigheim-bissingen'},{'time':'21:14','transport':'S4','direction':'backnang'},]



j_data = json.loads(json.dumps(data))

print (j_data)
for item in j_data:
    # now song is a dictionary
    for attribute, value in item.items():
        print attribute, value # example usage
