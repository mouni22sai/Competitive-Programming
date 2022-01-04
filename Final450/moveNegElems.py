def moveNegElems(l):
    start = 0
    end = len(l) - 1

    while start < end:
        if l[start] < 0:
            start = start + 1
        elif l[start] > 0:
            while l[end] > 0:
                end = end - 1
            temp = l[end]
            l[end] = l[start]
            l[start] = temp
            start = start + 1
            end = end - 1
    return l


print(moveNegElems(list(map(int, input().split()))))
