#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonal_difference(arr):
    # Write your code here
    tmp1 = 0
    tmp2 = 0
    for i in range(n):
        tmp1 += arr[i][i]
        tmp2 += arr[i][n - i - 1]

    ans = abs(tmp1 - tmp2)
    return ans


if __name__ == '__main__':
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonal_difference(arr)
    print(result)
