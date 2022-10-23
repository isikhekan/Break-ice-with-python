import time

before = time.time()

for i in range(100):
    x = 1+1

after = time.time()

print("running time", after-before)