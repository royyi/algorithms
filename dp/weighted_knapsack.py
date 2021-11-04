# Roy Yi
# 10/22/21
# Solve the weighted knapsack problem

# There are n items in a room, each with value v[i] and weight w[i].
# Your knapsack has capacity c. 

# What is the best way to pick items such that the value is maximized
# and the total weight of all the items is less than c?

def improved_knapsack(val, wt, N, W):
    dp = [0] * (W+1)

    for i in range(1, N+1):
        for j in range(W, 0, -1):
            if j - wt[i-1] >= 0:
                dp[j] = max(val[i-1] + dp[j - wt[i-1]], dp[j])

    return dp[W]

def solve_knapsack(val, wt, N, W):
    dp = [[0]*(W+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, W+1):
            if j - wt[i-1] >= 0:
                dp[i][j] = max(val[i-1] + dp[i-1][j - wt[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[N][W]

def main():
    # value and weight of items 1..n
    val = [60, 100, 120]
    wt = [1, 2, 3]

    print(solve_knapsack(val, wt, 3, 5))
    print(improved_knapsack(val, wt, 3, 5))

if __name__ == "__main__":
    main()

# dp[i][j] gives the maximum value using items 0..i-1 inclusive with maximum capacity j

# if item fits in capacity, the best choice is either to take the item or leave it
# otherwise, we have to leave it

# runtime: O(N*W)
# space complexity: O(N*W)


# improved knapsack:
# notice that the recurrence for row i only needs row i-1, 
# so we only need the current row and the row above

# if we build the next row in reversed order, then all the values from the prior row
# can be used to find the current row, so only a single array is needed
