import timeit
from matplotlib import pyplot as plt

def func(n, dict = {}):
    if n == 0 or n == 1:
        return n
    else:
        if n in dict.keys():
            return dict[n]
        value = func(n-1) + func(n-2)
        dict[n] = value    
    return value
    

def func_old(n):
    if n == 0 or n == 1:
        return n
    else:
        return func_old(n-1) + func_old(n-2)

def new():
    for i in range(35):
        time = timeit.timeit(lambda:func(i), number=1)
        new_times[i] = time

def old():
    for i in range(35):
        time = timeit.timeit(lambda:func_old(i),number=1)
        old_times[i] = time

if __name__ == '__main__':
    new_times = {}
    old_times = {}
    time_new = timeit.timeit(new, number=1)
    time_old = timeit.timeit(old, number=1)
    print("The time it took for the new (updated) function was:", time_new)
    print("\nThe time it took for the old function was:", time_old)
    fig, axs = plt.subplots(2)
    axs[0].scatter(new_times.keys(), new_times.values())
    axs[0].set_title("Timing for changed function")
    axs[1].scatter(old_times.keys(), old_times.values())
    axs[1].set_title("Timing for original function")
    plt.show()