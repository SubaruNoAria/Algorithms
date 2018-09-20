#Given an integer N, find an aggregate sum of all integer partitions of this number
#each partition does not contain any integer less than k

def countPartition(N, K):
    """Input: N = 10, K = 3
    Output: 50
    5 valid partitions:
    1): {10}
    2): {7, 3}
    3): {6, 4}
    4): {5, 5}
    5): {3, 3, 4}"""
    """Funtion returns total number of valid partitions of integer N
    """
    #Declaration of 2D dp array for memoization
    dp = [[0 for x in range(201)] for y in range(201)]
    #Initializing 2D dp array with -1, use this for 2D array for memoization
    for i in range(N + 1):
        for j in range(N + 1):
            dp[i][j] = -1
    #if this subproblem is already calculated, then return answer
    if dp[N][K] >= 0:
        return dp[N][K]
    #if N < K, no valid partition is possible
    if N < K:
        return 0

    #if N is between K to 2*K, then only one partition that is number N itself
    if N < 2*K:
        return 1

    #Initialize answer with 1 as number N itself is always a valid partition
    answer = 1
    #Iterate over K to N, find number of possible valid partitions recursively
    for i in range(K, N):
        answer += countPartition(N - i, i)

    #Memoization is done by storing this calculated answer
    dp[N][K] = answer
    return answer

print("Total Aggregate sum of all valid partitions: ", countPartition(10, 3) * 10)




