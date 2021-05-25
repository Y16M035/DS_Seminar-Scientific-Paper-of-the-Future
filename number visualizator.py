import json
import matplotlib.pyplot as plt
from collections import Counter

f = open("random numbers.json")
numbers = json.load(f)
counts = Counter(numbers)
fig = plt.figure(figsize=(10, 5))
plt.bar(counts.keys(), counts.values())

plt.xlabel("Number")
plt.ylabel("Count")
plt.title("Distribution of random numbers")
plt.savefig("visualization.png")

