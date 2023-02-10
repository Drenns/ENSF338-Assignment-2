import timeit

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
        func(i)

def old():
    for i in range(35):
        func_old(i)

if __name__ == '__main__':
    time_new = timeit.timeit(new, number=1)
    time_old = timeit.timeit(old, number=1)
    print("The time it took for the new (updated) function was:", time_new)
    print("\nThe time it took for the old function was:", time_old)

#not done