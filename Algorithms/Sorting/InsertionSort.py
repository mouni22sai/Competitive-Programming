# Insertion Sort algorithm

def insertionSort(l):
    n = len(l)

    for i in range(1, n):
        key = l[i]
        j = i-1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j = j-1
        l[j+1] = key
    return l


print(insertionSort(list(map(int, input().split()))))

# Time complexity of insertion sort = O(n^2)

