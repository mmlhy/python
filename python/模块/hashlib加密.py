import hashlib

m = hashlib.md5()
m.update('admin'.encode('utf-8'))
print(m.hexdigest())

s = hashlib.sha512()
s.update('admin'.encode('utf-8'))
print(s.hexdigest())

