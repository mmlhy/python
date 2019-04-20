"""
import json

info = {
    "name" : "miao",
    "age" : 20
}

f= open("json","w")
f.write(json.dumps(info))
f.close()
"""
#高级

import pickle

def anc():
    pass

info = {
    "name" : "miao",
    "age" : 20,
    "test": anc
}
f= open("json","wb")
f.write(pickle.dumps(info)) # pickle.dump(info,f)
f.close()
