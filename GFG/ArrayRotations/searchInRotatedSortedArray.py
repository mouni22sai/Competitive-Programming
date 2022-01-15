"""

Find the given element in a sorted and rotated array

    1) Find the minimum element in the array using binary search O(logN) time complexity
        based on the condition where just previous element is greater than it
    2) Use this as a pivot to partition the array
        Elements to the left of this key are all greater than the elements of the right of this key

    3) Find the partition array where the given element falls and do a binary search

"""


def findMinInSortedRotatedArray(l):
    n = len(l)
    start = 0
    end = n-1

    if l[start] <= l[end]:
        return l[start]

    while start <= end:
        mid = int((start+end)/2)

        if l[mid] < l[mid-1]:
            return l[mid]

        # if l[]



    return -1


print(findMinInSortedRotatedArray(list(map(int, input().split()))))



