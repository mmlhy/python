import json


info = {
    "name" : "miao",
    "age" : 20,
}
f= open("json","w")
f.write(json.dumps(info))
info['age'] = 33
f.write(json.dumps(info))
f.close()