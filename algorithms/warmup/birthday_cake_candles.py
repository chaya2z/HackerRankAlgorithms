#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthdayCakeCandles function below.
def birthday_cake_candles(ar):
    max_height = max(ar)
    num_max_height = ar.count(max_height)
    return num_max_height


if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthday_cake_candles(ar)
    print(result)
