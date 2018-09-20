#Two types of powers: A, B, three types of areas: X, Y, Z
#Every second switch areas, each area has specific properties
#by which your power A and power B increase or decrease
#keep choosing areas in such a way that our survival time maximal
#When A or B reaches less than 0, ends

#Need to memoize the result on basis of power A and B if reach to same pair of power A and B

#Class to represent an area
class area:
    def __init__(self, a, b):
        self.a = a
        self.b = b

#Utility method to get maximum survival time
def maxSurvival(A, B, X, Y, Z, last, memo):
    """Initial value of Power A = 20
        Initial value of Power B = 8

    Area X (3, 2) : If you step into Area X,
                A increases by 3,
                B increases by 2

    Area Y (-5, -10) : If you step into Area Y,
                   A decreases by 5,
                   B decreases by 10

    Area Z (-20, 5) : If you step into Area Z,
                  A decreases by 20,
                  B increases by 5

    It is possible to choose any area in our first step.
    We can survive at max 5 unit of time by following
    these choice of areas :
    X -> Z -> X -> Y -> X"""
    #if any of A or B is less than 0, return 0
    if A <= 0 or B <= 0:
        return 0
    cur = area(A, B)

    #if already calculated, return calculate value
    for ele in memo.keys():
        if cur.a == ele.a and cur.b == ele.b:
            return memo[ele]

    #step to areas on basis of last chosen area
    if last == 1:
        temp = 1 + max(maxSurvival(A + Y.a, B + Y.b,
                                   X, Y, Z, 2, memo),
                       maxSurvival(A + Z.a, B + X.b,
                                   X, Y, Z, 3, memo))
    elif last == 2:
        temp = 1 + max(maxSurvival(A + X.a, B + X.b,
                                   X, Y, Z, 1, memo),
                       maxSurvival(A + Z.a, B + Z.b,
                                   X, Y, Z, 2, memo))
    elif last == 3:
         temp = 1 + max(maxSurvival(A + X.a, B + X.b,
                                    X, Y, Z, 1, memo),
                        maxSurvival(A + Y.a, B + Y.b,
                                    X, Y, Z, 2, memo))
    # store the result into map
    memo[cur] = temp

    return temp

#method returns maximum survival time
def getMaxSurvivalTime(A, B, X, Y, Z):
    if A <= 0 or B <= 0:
        return 0
    memo = dict()

    #At first, can be any of the area
    return max(maxSurvival(A + X.a, B + X.b, X, Y, Z, 1, memo),
               maxSurvival(A + Y.a, B + Y.b, X, Y, Z, 2, memo),
               maxSurvival(A + Z.a, B + Z.b, X, Y, Z, 3, memo))

X = area(3, 2)
Y = area(-5, -10)
Z = area(-20, 5)
A = 20
B = 8
print(getMaxSurvivalTime(A, B, X, Y, Z))
