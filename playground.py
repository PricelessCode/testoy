from testoy.test_sort import decorator_sort
from testoy.build_sort_case import build_sort_case

# The sorting array has to take only an array and have to return the sorted array.
@decorator_sort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubbleSort([1, 2])