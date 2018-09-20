#Given a fence n posts and k colors, find out the number of ways of painting the fence at most 2 adjacent posts have same color
#total[i] = same[i] + diff[i]
#same[i] = diff[i-1]
#diff[i] = (diff[i-1] + diff[i-2])*(k-1)
# = total[i-1]*(k-1)

#Returns count of ways to color k posts using k colors
def countWays(n, k):
    """Input: n = 2, k = 4
    Output: 16
    both posts have same color: 4
    both posts have diff color:
    4 * 3 = 12

    Input: n = 3, k = 2
    Output: 6
    both posts have sanme color: 3
    both posts have diff color: 3
    """

    #To store results for subproblems
    dp = [0 for i in range(n+1)]
    #k ways to color first post
    dp[1] = k
    #0 ways for single post to voilate (same color and k ways to not voilate)
    same = 0
    diff = k
    #Fill for 2 posts onwards
    for i in range(2, n+1):
        #Current same is same as previous diff
        same = diff
        #always have k-1 choices for next post
        diff = dp[i-1] * (k-1)
        #Total choices till i
        dp[i] = same + diff
    return dp[n]

n = 2
k = 4
print("Number of ways: ", countWays(n, k))


#Optimization
def countWays1(n, k):
    #k ways to color first post
    total = k
    #0 ways for single post to voilate
    same = 0
    diff = k
    #Fill for 2 posts onwards
    for i in range(2, n+1):
        #Current same is same as previous diff
        same = diff
        #always have k-1 choices for next post
        diff = total * (k-1)
        #total choices till i
        total = same + diff
    return total
n = 2
k = 4
print("Number of ways: ", countWays1(n, k))



