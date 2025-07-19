# this is the code about insertion sort in python

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = i
        temp = arr[i]
        while key > 0 and arr[key-1] > temp:
            arr[key] = arr[key-1]
            key -= 1
            print(f"key: {key}, temp: {temp}, arr: {arr}")
        arr[key] = temp
        print(f"key: {key}, temp: {temp}, arr: {arr} ----------------------------------------------------------------------------")
arr = [10, 4, 43, 5, 57, 91, 45, 9, 7]
insertionSort(arr)
print(arr)

 