# Selection sort algorithm
def selectionSort(l):

    n = len(l)
    for i in range(0, n):
        indexOfActualMin = i
        for j in range(i+1, n):
            if l[j] < l[indexOfActualMin]:
                indexOfActualMin = j
        temp = l[i]
        l[i] = l[indexOfActualMin]
        l[indexOfActualMin] = temp

    return l


print(selectionSort(list(map(int, input().split()))))

# the inner loop runs n-1 + n-2 + .....1 which is n(n-1)/2 times
# Time complexity of this program = Theta(n^2)

