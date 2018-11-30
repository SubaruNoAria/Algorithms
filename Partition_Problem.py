#Partition problem is to determine whether a given set can be partitioned into two subsets such that
#the sum of elements in both subsets is same

#We need to:
#1. Calculate sum of the array. If sum is odd, then there can not be two subsets with equal sum
#2. If sum of array elements is even, calculate sum/2 and find a subset of array with sum equal to sum/2

def isSubsetSum(arr, n, su,):
    """
    arr[] = {1, 5, 11, 5}
    Output = True
    The array can be partitioned as {1, 5, 5} and {11}
    """
    #base case
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    # if last element is greater than sum, then ignore it
    if arr[n-1] > sum:
        return isSubsetSum(arr, n-1, sum)

    '''else check if sum can be obtained by any of including/excluding the last element
    '''
    return isSubsetSum(arr, n-1, sum) or isSubsetSum(arr,n-1, sum-arr[n-1])

#Return true is arr[] can be partitioned in two
#subsets of equal sum, otherwise false

def findPartion(arr, n):
    #Calculate sum of the elements in array
    sum = 0
    for i in range(0, n):
        sum += arr[i]
    #If sum is odd, there cannot be two subsets with equal sum
    if sum % 2 != 0:
        return False

    #Find if there is subset with sum equal to half of total sum
    return isSubsetSum(arr,n,sum //2)

arr = [3,1,5,9,12]
n = len(arr)
if findPartion(arr,n) == True:
    print("can be divided")
else:
    print("can not be divided")
