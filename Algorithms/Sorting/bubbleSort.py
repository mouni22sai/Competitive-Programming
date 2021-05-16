# normal bubble sort
def normalBubbleSort(l):
    n = len(l)
    for i in range(0, n-1):
        for j in range(0, n-1):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp

    return l


print(normalBubbleSort(list(map(int, input().split()))))

# Time Complexity = O(n^2)
# Space complexity = O(1)

# NUmber of times the inner loop runs = n-1 + n-1 + n-1 +........+ n-1 for n-1 times which is (n-1)^2


# optimized bubble sort
def optimizedBubbleSort(l):
    n = len(l)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                # swap these two
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    return l


print(optimizedBubbleSort(list(map(int, input().split()))))

# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Number of times the inner loop runs n-1 + n-2 + n-3 + n-4 + ........1 = n(n+1)/2


# further optimized bubble sort
def furtherOptimizedBubbleSort(l):
    n = len(l)
    for i in range(0, n-1):
        swapped = False
        for j in range(0, n-1-i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
                swapped = True
        if not swapped:
            break

    return l


print(furtherOptimizedBubbleSort(list(map(int, input().split()))))

# In this optimization, the inner loop runs only until array is sorted. Once array is sorted
# the executions stops and returns the sorted array. Saves many number of operations.
# Worst case time complexity = O(n^2)


