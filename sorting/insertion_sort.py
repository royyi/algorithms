# Roy Yi
# 10/13/21
# Code inserion sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j-1 >= 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr

print(insertion_sort([3, 20, 5, 16, 8, 4, 2, 9]))
