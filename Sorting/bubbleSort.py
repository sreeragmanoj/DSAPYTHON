# This is a bubble sort implementation in python

import time

start_time = time.time()


def bubbleSort(arr):
    start_time = time.time()
    for passnum in range(len(arr)-1, 0, -1):
        print(f"passnum: {passnum}")
        for i in range(passnum):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    return arr


arr = [5, 4, 3, 2, 1]
print(bubbleSort(arr))


# in here the best case is also O(n^2) we can use a flag to check if the array is already sorted or not that will make the best case O(n)

def bubbleSoerWithFlag(arr):
    start_time = time.time()
    swapped = 1
    for passnum in range(len(arr)-1, 0, -1):
        print(f"passnum: {passnum}")
        if swapped == 0:
            return
        for i in range(passnum):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = 1
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    return arr

print(bubbleSoerWithFlag(arr))