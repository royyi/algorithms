# Roy Yi
# 9/27/21
# find the maximum subarray sum using kadane's algorithm

def max_subarray(arr):
    best = 0
    local_max = 0

    for num in arr:
        local_max = max(num, local_max + num)

        if local_max > best:
            best = local_max

    return best


def main():
    print(max_subarray([-5, 2, 5, -7, 8, -4, 20])) 

if __name__ == "__main__":
    main()

# kadane's algorithm: local_max[i] = max(arr[i], local_max[i-1] + arr[i])

# essentially, the best subarray is either starting from a previous position,
# or restarting here

# algorithm allows for empty subarray (best = 0), otherwise set best to -inf 
