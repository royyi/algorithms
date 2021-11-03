# Roy Yi
# 10/24/21
# Implement in-place mergesort

def merge(arr, start, mid, end):
    '''merge arrays [start..mid] and [mid+1..end] in sorted order in arr'''
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]

    i = j = 0 
    k = start
    while i < len(left) and j < len(right):
        if left[i] < right[j]: 
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # place remaining elements at end of array
    while i < len(left): 
        arr[k] = left[i]
        i += 1; k += 1

    while j < len(right): 
        arr[k] = right[j]
        j += 1; k += 1

def mergesort(arr, start, end):
    if start < end:
        mid = (start+end)//2
        mergesort(arr, start, mid)
        mergesort(arr, mid+1, end)
        merge(arr, start, mid, end)

def main():
    arr = [8, 5, 3, 9, 1, 10, 8, 7]
    mergesort(arr, 0, len(arr)-1)
    print(arr)

if __name__ == "__main__":
    main()
