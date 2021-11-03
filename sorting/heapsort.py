# Roy Yi
# 10/25/21
# Implement heapify algorithm and heapsort

def percolate_down(arr, i):
    # left and right child indices (0 indexed heap)
    left = 2*i+1; right = 2*i+2

    # while node has child (must be on left)
    while left < len(arr): 
        child = left
        if right < len(arr) and arr[right] < arr[left]:
            child = right

        # swap current node with the smaller child (if necessary)
        if self.arr[child] < arr[i]
            arr[child], arr[i] = arr[i], arr[child]
        else:
            break

        n = child

def heapify(arr, N=len(arr)):
    '''Converts arr into a max heap.'''
    for i in reversed(range(N//2)):
        percolate_down(arr, i)

def heapsort(arr):
    N = len(arr)
    heapify(arr)
    for i in reversed(range(N)):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i)
        percolate_down(arr, 0)
