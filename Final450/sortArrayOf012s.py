def sorted012s(l):
    i = 0
    j = len(l) - 1

    # indices 0 to i-1 contain 0s, i to j contain 1s, j+1 to n-1 contain 2s

    start = 0

    while start <= j:
        if l[start] == 1:
            start = start + 1
        if l[start] == 0:
            l[start] == l[i]
            l[i] = 0
            i = i + 1
            start = start + 1
        if l[start] == 2:
            l[start] = l[j]
            l[j] = 2
            j = j - 1
    return l


print(sorted012s(list(map(int, input().split()))))

# lengthA = len(arr)
# count0 = 0
# count1 = 0
# count2 = 0
# for i in range(lengthA):
#     if arr[i] == 0:
#         count0 = count0 + 1
#     if arr[i] == 1:
#         count1 = count1 + 1
#     if arr[i] == 2:
#         count2 = count2 + 1
#
# for i in range(lengthA):
#     if i < count0:
#         arr[i] = 0
#     if i >= count0 and i < count0 + count1:
#         arr[i] = 1
#     if i >= count0 + count1:
#         arr[i] = 2
