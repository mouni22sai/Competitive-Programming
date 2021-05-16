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
