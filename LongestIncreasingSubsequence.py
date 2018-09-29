#Longest increasing subsequence is to find the length of the longest subsequence of a given sequence
#Such that all elements of the subsequence are sorted in increasing order

#There are two ways to solve this
#1. Optimal Substructure
#Let arr[0...n-1] be the input array and L(i) be the length of LIS ending
# at in dex i such that arr[i] is the last element of the LIS

#L(i_ can be recursively written:
# L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
# L(i) = 1, if no such j exists.

#To find the LIS for a given array, we need to return max(L(i)) where 0 < i < n.

"""
This function return two things:
(1) Length of LIS ending with element arr[n-1].
(2) Overall maximum as the LIS may end with an element
before arr[n-1] maximum numer is used
LIS values of full array of size n in stored in max_ref
"""

#Set global variable to store the maximum
global maximum

def list1(arr, n):
    #Access to global variable
    global maximum

    #Base
    if n == 1:
        return 1

    #LIS length ending with arr[n-1]
    maxLIS = 1

    """Get all LIS ending with arr[0], ..., arr[n-2]
     If arr[i-1] is smaller than arr[n-1], then maximum ending
     with arr[n-1] needs to be updated"""
    for i in range(1, n):
        res = list1(arr, i)
        if arr[i-1] < arr[n-1] and res + 1 > maxLIS:
            maxLIS = res + 1

    #Compare maxLIS with overall maximum, update if needed
    maximum = max(maximum, maxLIS)

    return maxLIS

def list2(arr):
    #Access to global variable
    global maximum

    #Length of arr
    n = len(arr)

    #Maximum variable holds the result
    maximum = 1

    #The function list1() stores its result in maximum
    list1(arr, n)

    return maximum

arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
n = len(arr)
print("Length of list is ", list2(arr))

#Overlapping Subproblem
#There are many subproblems being solved repeatly. It can be avoided by
#using Memoization or Tabulation

#list2 returns length of the longest increasing subsequence
#in array of size n
def list2(arr):
    n = len(arr)

    #Declare the list for LIS and initialize LIS value
    #for all indexes
    list2 = [1] * n

    #Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(1, n):
            if arr[i] > arr[j] and list2[i] < list2[j] + 1:
                list2[i] = list2[j] + 1

    #Initialize maximum to 0 to get the maximum of all LIS
    maximum = 0

    #Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, list2[i])

    return maximum

arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of lis is", list2(arr))