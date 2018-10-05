#Given 3 strings, find the longest common subsequence in all three given sequences

#Take a 3D array to store the length of common subsequence in all 3 given sequences
#L[m+1][n+1][l+1]
#1. If any of the string is empty then no common subsequence
#   L[i][j][k] = 0

#2. If the characters of all sequences match
# X[i] == Y[j] == Z[k], then
#L[i][j][k] = 1+ l[i-1][j-1][k-1]

#3. If the characters of both sequences do not match
#X[i] != Y[j] | X[i] != Z[k] | Y[j] != Z[k], then
#L[i][j][k] = max(L[i-1][j][k], L[i][j-1][k], L[i][j][k-1])

def lcs3s(X, Y, Z, m, n, o):
    """
    Input: str1 = "abcd1e2"
            str2 = "bc12ea"
            str3 = "bd1ea"
    Output: 3
    Longest Common subsequence is ble
    """
    L = [[[0 for i in range(o+1)] for j in range(n+1)] for k in range(m+1)]

    """
    We will do this in bottom up way
    L[i][j][k] contains length of LCS of X[0...i-1], 
    Y[0...j-1], Z[0...k-1]
    """
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if i == 0 or j == 0 or k == 0:
                    L[i][j][k] = 0

                elif X[i-1] == Y[j-1] and X[i-1] == Z[k-1]:
                    L[i][j][k] = L[i-1][j-1][k-1] + 1

                else:
                    L[i][j][k] = max(max(L[i - 1][j][k],
                                     L[i][j - 1][k]),
                                     L[i][j][k - 1])


    #L[m][n][o] contains length of LCS for X[0..n-1] and Y[0..m-1] and Z[0..o-1]
    return L[m][n][o]


X = 'AGGT12'
Y = '12TXAYB'
Z = '12XBA'

m = len(X)
n = len(Y)
o = len(Z)

print('Length of LCS is', lcs3s(X, Y, Z, m, n, o))