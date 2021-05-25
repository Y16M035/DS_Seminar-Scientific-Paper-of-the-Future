import random
import json

f = open('random numbers.json', 'w')
json.dump([random.randint(0,100) for i in range(1000)], f)
f.close()