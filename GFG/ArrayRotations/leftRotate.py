import copy


def leftRotate(l, d):
    n = len(l)
    k = copy.deepcopy(l)
    for i in range(n-d):
        l[i] = k[d+i]
    for i in range(n-d, n):
        l[i] = k[i-n+d]

    return l


print(leftRotate(list(map(int, input().split())), int(input())))

# O(n) Time Complexity and O(n) extra space
