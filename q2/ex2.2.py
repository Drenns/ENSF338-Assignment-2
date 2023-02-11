import sys
import time
import json
from matplotlib import pyplot as plt

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open("ex2.json", "r") as jsonfile:
    data_file = json.load(jsonfile)

alltimes = {}
for i in range(10):
    start_time = float(time.time())
    func1(data_file[i], 0, 999)
    end_time = float(time.time())
    alltimes[i] = (end_time - start_time)
print(alltimes)

plt.scatter(alltimes.keys(), alltimes.values())
plt.xlabel("Data set number")
plt.ylabel("Time in seconds")
plt.title("Sorting Performance")
plt.show()