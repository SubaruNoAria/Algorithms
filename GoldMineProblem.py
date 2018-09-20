#A n*m dimension. Each field in this mine as a positive integer.
#Initially the miner is at first column but can be at any row
#Move only (right -> right up/right down), move to the cell diagonally up towards the right or right or diagonally down
#towards the right. Find out maximum amount of gold

#1. Amount of gold is positive, cover maximum cells of maximum values under given constraints
#2. Move one step toward right side. Always end up in last column.

#Top-down, memoization way

import numpy as np
def getMaxGold(gold, m, n):
    """Returns maximum amount of gold that can be collected
    when started from first column and moves allowed are right, right-up and right-down"""
    """Create a table for storing intermediate results and initialize all cells to 0.
    The first row of goldMineTable gives the maximum gold that the miner can collect when starts that row
    """
    """Input: mat[][] = {{1, 3, 3},
                         {2, 1, 4},
                         {0, 6, 4}}
        Output: 12
        {(1, 0) -> (2, 1) -> (2, 2)}"""
    #Here, can not use 4*[4*[0]], this will create a matrix that each column use the same row
    goldTable = [[0 for i in range(n)]
                 for j in range(m)]
    for col in range(n-1, -1, -1):
        for row in range(m):
            #For gold collected on going to the cell on the right
            if col == n-1:
                right = 0
            else:
                right = goldTable[row][col+1]
            #Gold collected on going to cell to right up
            if row == 0 or col == n-1:
                right_up = 0
            else:
                right_up = goldTable[row-1][col+1]
            #Gold collected on going to cell to right down
            if row == m-1 or col == n-1:
                right_down = 0
            else:
                right_down = goldTable[row+1][col+1]
            #Max gold collected on either way
            goldTable[row][col] = gold[row][col] + max(right, right_up, right_down)

        #The max amount collected will be the max value in first column of all rows
    res = goldTable[0][0]
    for i in range(1, m):
        res = max(res, goldTable[i][0])

    #Another way to do this is using numpy to select the maximum number in first column of all rows
    a = np.array(goldTable, dtype = int)
    res = a.max(axis = 0)[0]

    return res


gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]

m = 4
n = 4

print(getMaxGold(gold, m, n))




