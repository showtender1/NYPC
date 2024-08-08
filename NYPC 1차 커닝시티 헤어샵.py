def min_sum(n, arr):
    if n == 1:
        return arr[0]

    dp = [0] * n

    dp[0] = arr[0]

    dp[1] = min(arr[0] + arr[1], max(arr[0], arr[1]))

    for i in range(2, n):
        option1 = dp[i - 1] + arr[i]
        option2 = dp[i - 2] + max(arr[i - 1], arr[i])
        dp[i] = min(option1, option2)

    return dp[-1]

n = int(input())
arr = list(map(int, input().split()))

print(min_sum(n, arr))
