import zlib

s = 'hello world!hello world!hello world!hello world!'
t = bytes(s,"utf-8")
y = zlib.compress(t)


print(y)
print(zlib.decompress(y))