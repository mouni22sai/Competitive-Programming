# Finding min and max in an array
def maxAndMin(l):
    minL = l[0]
    maxL = l[0]

    for i in range(1, len(l)):
        if l[i] < minL:
            minL = l[i]
        if l[i] > maxL:
            maxL = l[i]

    print(minL)
    print(maxL)
    return


maxAndMin(list(map(int, input().split())))
