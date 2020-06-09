#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def mini_max_sum(arr):
    ans = [0, 0]
    arr = sorted(arr)
    ans[0] = sum(arr[:-1])
    ans[1] = sum(arr[1:])
    return ans[0], ans[1]


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    ans = mini_max_sum(arr)
    print(ans[0], ans[1])

