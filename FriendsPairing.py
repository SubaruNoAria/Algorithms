#Given n friends, each one can remain single or paired up.
#Each can only be paired once. Find the total number of ways remain single or paired up

#There are f(n) = ways n people can remain single or pair up
#For n-th person there are two choinces:
#1) n-th person remains single, recur for f(n-1)
#2) n-th person pairs up with any of the remaining n-1 persons. Then (n-1)*f(n-2)

#f(n)  = f(n-1) + (n-1)*f(n-2)

def countFriendsPairing(n):
    """Input: n = 3
    Output: 4
    1: {1}, {2}, {3}
    2: {1}, {2, 3}
    3: {1, 2}, {3}
    4: {1, 3}, {2}"""
    dp = [0 for i in range(n+1)]
    # Filling dp[] in bottom up manner
    # Using recursive formula explained above
    for i in range(n):
        if i <= 2:
            dp[i] = i
        else:
            dp[i] = dp[i-1] + (i-1)*dp[i-2]

    return dp[n]

n = 4
print(countFriendsPairing(n))