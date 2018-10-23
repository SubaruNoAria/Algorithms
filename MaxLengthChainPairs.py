# Given n pairs of numbers, the first number is always smaller than the
# second number. A pair (c,d) can follow another pair(a,b) if b<c.

#Find the longest chain which can be formed from a given set of pairs

# 1. Sort given pairs in increasing order of first element
# 2. Run modified LIS process where compare the second element of already finalized LIS
# with the first element of new LIS being constructed

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

# Assumes that arr[] is sorted in increasing order
# according the first values in pairs.
def maxChainLength(arr, n):
    """Input: {{5, 24},
    {39, 60},
    {15, 28},
    {27, 40},
    {50, 90}}

    Output:  {{5, 24}, {27, 40}, {50, 90}}"""
    max = 0

    # Initialize max chain length values for all indices
    mcl = [1 for i in range(n)]

    # Compute optimized chain length values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if (arr[i].a > arr[j].b and mcl[i] < mcl[j] + 1):
                mcl[i] = mcl[j] + 1
    # mcl[i] now stores the maximum
    # chain length ending with pair i

    # Pick maximum of all MCL values
    for i in range(n):
        if max < mcl[i]:
            max = mcl[i]

    return max

# Test

arr = [Pair(5, 24),
       Pair(15, 25),
       Pair(27, 40),
       Pair(50, 60)]

print('Length of maximum size chain is',
      maxChainLength(arr, len(arr)))