# this is the code for selection sort

import time

def selectionSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        LVIndex = 0
        for j in range(1, i+1):
            if arr[j] > arr[LVIndex]:
                LVIndex = j
        arr[i], arr[LVIndex] = arr[LVIndex], arr[i]

arr = [5, 4, 3, 2, 1]
selectionSort(arr)
print(arr)