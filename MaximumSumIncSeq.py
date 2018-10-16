#Given an array of n positive intergers, find the sum of maximum
#sum subsequence of the given array such that the integers in the subsequence
#are sorted in increasing order

# Input: {1, 101, 2, 3, 100, 4, 5}
# Output: {106: 1, 2, 3, 100}

#This is a variatio of standard Longest Increasing Subsequence problem

def MaxSumIS(arr, n):
    max = 0
    msis = [0 for x in range(n)]

    # Initialize msis values
    # for all indexes

    for i in range(n):
        msis[i] = arr[i]

    # Compute maximum sum
    # values in botton up manner
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and msis[i] < msis[j] + arr[i]:
                msis[i] = msis[j] + arr[i]

    # Pick maximum of all msis values
    for i in range(n):
        if max < msis[i]:
            max = msis[i]

    return max

arr = [1, 101, 2, 3, 100, 4, 5]
n = len(arr)
print("Maximum sum increasing subsequence is: ", str(MaxSumIS(arr, n)))

