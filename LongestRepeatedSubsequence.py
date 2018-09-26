# Given a string, return the longest repeating subsequence such that the two subsequence don't have same string character at same position
#It is modified longest common subsequence
# To find the LCS(str, str) where str is the input string with the restriction that when both the characters are same
# They shouldn't be on the same index in the two strings

def LRS(str):
    """Input: str = "aabb"
        Output: "ab"
    """
    n = len(str)

    #Create and initialize DP table
    dp = [[0 for k in range(n+1)] for l in range(n+1)]

    #Fill DP table
    for i in range(1, n+1):
        for j in range(1, n+1):
            # If characters match and indices are not same
            if (str[i-1] == str[j-1] and i != j):
                dp[i][j] = 1 + dp[i-1][j-1]

            # If characters do not match
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    # To find the result string using dp[][] initialize result
    res = ''

    # Traverse dp[][] from bottom right
    i = n
    j = n
    while (i > 0 and j > 0):
        # If this cell is same as diagonally
        # adjacent cell just above it, then
        # same characters are present at
        # str[i-1] and str[j-1]. Then append any
        # of them to result
        if dp[i][j] == dp[i-1][j-1] + 1:
            res += str[i-1]
            i -= 1
            j -= 1

        #Otherwise, move to the side to give maximum result
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j -= 1

    # get result in reverse order
    res = ''.join(reversed(res))

    return res

str = 'AABEBCDD'
print(LRS(str))

