import sys
import threading
import json
import matplotlib.pyplot as plt
import time
import random
sys.setrecursionlimit(20000)
threading.stack_size(33554432)

with open("ex2.json", 'r') as data_file:
    data = json.load(data_file)

def func1(array, start, end):
    if start < end:
        pivotIndex = func2(array, start, end)
        func1(array, start, pivotIndex - 1)
        func1(array, pivotIndex + 1, end)

def func2(array, start, end):
    pivot = random.choice(array[start:end + 1])
    low = start
    high = end
    while low <= high:
        while array[low] < pivot:
            low += 1
        while array[high] > pivot:
            high -= 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
            low += 1
            high -= 1
    return low

time_dict = {}
i = 0

for array in data:
    start_time = float(time.time())
    func1(array, 0, len(array)-1)
    end_time = float(time.time())
    total_time = float(end_time - start_time)
    time_dict[i] = total_time
    i += 1

print(time_dict)
    
plt.scatter(time_dict.keys(), time_dict.values())
plt.xlabel("Array Number")
plt.ylabel("Time in seconds (s)")
plt.show()