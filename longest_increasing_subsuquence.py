def longest_increasing_subsequence_length(A):
    if not A:
        return 0
    
    n = len(A)
    dp = [1] * n                 # dp[i] = answer ending at i
    
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i]:      # can extend from j to i
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)