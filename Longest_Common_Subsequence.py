#Given two sequences, find the length of longest subsequence present in both of them
# It is a classic computer science problem, the basis of diff and has application in bioinformatics

#1). Optimal Substructure:
# Input sequences: X[0...m-1] and Y[0...n-1] length: m and n
# If last characters of both sequences match (X[m-1] == Y[n-1])
# then L(X[0...m-1], Y[0...n-1]) = 1 + L(X[0...m-2], Y[0...n-2])

#If not:
# L(X[0..m-1], Y[0..n-1]) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2]) )

#2). Overlapping Subproblems

# Naive recursive implementation of LCS problem
def lcs(X, Y, m, n):
    """Input: Sequences ABCDHG, AEDFHR
        Output: ADH, length 3.

        Input: Sequences AGGTAB, GXTXAYB
        Output: GTAB, length 4."""
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y, len(X), len(Y)))

#The time complexity is O(2^n)


# A faster way is tabulated implementation, t avoid solve the sequence twice
def lcs1(X, Y):
    # define the length
    m = len(X)
    n = len(Y)

    # declaring the array for storing values
    L = [[None] * (n+1) for i in range(m+1)]

    # build L[m+1][n+1] in bottom up manner
    # L[i][j] contains length of LCS of X[0...i-1] and Y[0...j-1]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    #L[m][n] contains the length of LCS of X[0..n-1] and Y[0..m-1]
    return L[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs1(X, Y))

# Time complexity of the implementation is O(m)(n)