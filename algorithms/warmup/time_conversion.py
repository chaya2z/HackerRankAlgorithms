#!/bin/python3
import os
import sys


#
# Complete the timeConversion function below.
#
def time_conversion(s):
    #
    # Write your code here.
    #
    if s[-2:] == 'AM':
        if s[:2] == '12':
            ans = '00' + s[2:-2]
            return ans
        return s[:-2]
    else:
        if s[:2] == '12':
            ans = s[:-2]
            return ans
        s_list = list(s)
        hour = int(s[:2])
        hour += 12
        s_list[:2] = [str(hour)[0], str(hour)[1]]
        ans = ''.join(s_list[:-2])
        return ans


if __name__ == '__main__':
    s = input()
    result = time_conversion(s)
    print(result)
