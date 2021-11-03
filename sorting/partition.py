# Roy Yi
# 10/23/21
# Implement in-place partition

from random import randint

def partition(arr, start, end):
    '''partition array into left portion smaller than the pivot, and right
    portion larger than the pivot. Pick the ending element as the pivot.'''
    pivot = arr[end]

    i = start
    for j in range(start, end):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[end] = arr[end], arr[i]
    return i

def randomized_partition(arr, start, end):
    '''place random pivot at the start'''
    v = randint(start, end)
    arr[end], arr[v] = arr[v], arr[end]
    return partition(arr, start, end)

def main():
    arr = [10, 2, 8, 7, 1, 3, 5, 6, 4, 8, 4]
    v = randomized_partition(arr, 0, len(arr)-1)
    print(f"{v}:", arr)

if __name__ == "__main__":
    main()

'''
def partition(arr, i, j):
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
'''
