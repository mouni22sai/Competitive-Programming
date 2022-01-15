def binarySearch(l, x):
    n = len(l)
    start = 0
    end = n-1

    while start <= end:
        mid = int((start + end) / 2)
        if l[mid] > x:
            end = mid - 1
        elif l[mid] < x:
            start = mid + 1
        elif l[mid] == x:
            return mid

    return None


print(binarySearch(list(map(int, input().split())), int(input())))
