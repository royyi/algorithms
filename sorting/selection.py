# Roy Yi
# 10/23/21
# Implement randomized selection

from random import randrange

def partition(arr, pivot_idx):
    pivot = arr[pivot_idx]
    left, equal, right = [], [], []

    for num in arr:
        if num < pivot: left.append(num)
        if num == pivot: equal.append(num)
        else: right.append(num)

    return left, equal, right

def selection(arr, k):
    '''return kth smallest value in arr, elements may be repeated'''
    v = randrange(len(arr))
    left, equal, right = partition(arr, v)

    if k <= len(left):
        return selection(left, k)

    elif k <= len(left) + len(equal):
        return arr[v]

    return selection(right, k - len(left) - len(equal))

def main():
    arr = [2, 5, 7, 4, 3, 8]
    print(selection(arr, 3))

if __name__ == "__main__":
    main()
