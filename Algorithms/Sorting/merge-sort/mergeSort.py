# Merge two sorted parts of an array

def merge(l, low, mid, high):
    left = []
    right = []

    for i in range(low, mid+1):
        left.append(l[i])

    for i in range(mid+1, high+1):
        right.append(l[i])

    i = 0
    j = 0
    k = low

    while i < mid - low + 1 and j < high - mid:
        if left[i] <= right[j]:
            l[k] = left[i]
            i = i + 1
        else:
            l[k] = right[j]
            j = j + 1
        k = k + 1

    while i < mid - low + 1:
        l[k] = left[i]
        i = i + 1
        k = k + 1

    while j < high - mid:
        l[k] = right[j]
        j = j + 1
        k = k + 1


def mergeSort(l, low, high):

    if low < high:
        mid = int((high + low)/2)
        mergeSort(l, low, mid)
        mergeSort(l, mid+1, high)
        merge(l, low, mid, high)

    return l


li = list(map(int, input().split()))
print(mergeSort(li, 0, len(li) - 1))

# Time complexity of this solution is O(nlogn) where n is high-low+1
# Space complexity of this solution is O(n) where n is high-low+1

