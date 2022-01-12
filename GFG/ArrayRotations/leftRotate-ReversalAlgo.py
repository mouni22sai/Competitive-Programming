"""
    Reversal Algorithm takes O(n) time and O(1) space

    1) d Left Rotations
    Step1: Reverse the whole array
    Step2: Reverse subarray 0:n-d-1
    Step3: Reverse the remaining subarray n-d:n-1

    2) d Right Rotations
    Step1: Reverse the whole array
    Step2: Reverse the subarray 0:d-1
    Step3: Revere the subarray d:n-1

"""

import copy


def reverseArray(l, start, end):
    while start < end:
        temp = l[start]
        l[start] = l[end]
        l[end] = temp
        start = start + 1
        end = end - 1


def leftRotateConstantSpaceApproach(l, d):
    n = len(l)
    reverseArray(l, 0, n-1)
    reverseArray(l, 0, n-d-1)
    reverseArray(l, n-d, n-1)

    return l


def rightRotateConstantSpaceApproach(l, d):
    n = len(l)
    reverseArray(l, 0, n-1)
    reverseArray(l, 0, d-1)
    reverseArray(l, d, n-1)

    return l


li = list(map(int, input().split(" ")))
nd = int(input())

ri = copy.deepcopy(li)
print(leftRotateConstantSpaceApproach(li, nd))

print(rightRotateConstantSpaceApproach(ri, nd))

