# Roy Yi
# 10/24/21
# Find if a number exists in a sorted array (if so return its index)

def binary_search(arr, x, low, high):
    if low > high:
        return -1

    mid = (low+high) // 2

    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binary_search(arr, x, mid+1, high)

    return binary_search(arr, x, low, mid-1)

def main():
    arr = [1, 1, 2, 5, 8, 10, 20]
    print(binary_search(arr, 200, 0, len(arr)-1))


if __name__ == "__main__":
    main()


'''iterative binary search:

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
'''
