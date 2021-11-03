# Roy Yi
# 10/23/21
# Implement quicksort

from random import randint

def partition(arr, i, j):
    '''partition array into left portion smaller than the pivot, and right
    portion larger than the pivot. Pick the starting element as the pivot.'''
    start = i
    pivot = arr[i]

    while True:
        while i < len(arr) and arr[i] <= pivot: i += 1
        while arr[j] > pivot: j -= 1

        if i >= j: 
            break

        arr[i], arr[j] = arr[j], arr[i]
        
    arr[start], arr[j] = arr[j], arr[start]

    return j

def randomized_partition(arr, i, j):
    '''place random pivot at the start'''
    pivot = randint(i, j)
    arr[i], arr[pivot] = arr[pivot], arr[i]
    return partition(arr, i, j)

def quicksort(arr, start, end):
    if start < end:
        pivot_idx = randomized_partition(arr, start, end)
        quicksort(arr, start, pivot_idx-1)
        quicksort(arr, pivot_idx+1, end)

def main():
    arr = [4, 2, 8, 7, 1, 3, 5, 6, 4, 8, 10]
    quicksort(arr, 0, len(arr)-1)
    print(arr)

if __name__ == "__main__":
    main()
