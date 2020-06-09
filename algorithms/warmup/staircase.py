#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the staircase function below.
def staircase(n):
    space = " "
    sharp = "#"
    for i in range(1, n + 1):
        print(space * (n - i) + sharp * i)


if __name__ == '__main__':
    n = int(input())

    staircase(n)
