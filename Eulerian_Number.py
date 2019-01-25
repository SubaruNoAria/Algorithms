#The Eulerian number A(n, m) is the number of permutations of the numbers 1 to n in which exactly m elements
#are greater than previous element

#There are 4 permutations of the number 1 to 3 in which exactly 1 element is greater than the previous elements
132, 213, 231, 312
#Input: n = 3, m = 1
#Output: 4

def eulerian(n, m):
    if m>= n or n == 0:
        return 0

    if m == 0:
        return 1

    return ((n - m) * eulerian(n-1, m-1) +
            (m + 1) * eulerian(n - 1, m))

n = 3
m = 1
print(eulerian(n, m))