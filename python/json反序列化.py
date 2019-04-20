"""
import json

f = open("json","r")

data = json.loads(f.read())

print(data['age'])
f.close()

"""

#传高级的
import pickle

def anc():
    pass
f = open("json","rb")

data = pickle.loads(f.read()) #data = pickle.load(f)

print(data["test"]())
f.close()
