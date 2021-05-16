# normal bubble sort
def bubbleSort(l):
    n = len(l)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                # swap these two
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    return l


print(bubbleSort(list(map(int, input().split()))))

# Time Complexity = O(n^2)
# Space Complexity = O(1)

# The inner loop runs n-1 + n-2 + n-3 + n-4 + ........1 = n(n+1)/2
