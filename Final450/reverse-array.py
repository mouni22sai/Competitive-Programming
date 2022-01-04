def reverse(l):
    for i in range(len(l)):
        print(l[len(l)-1-i])
    return l


def reverseString(s):
    p = ''
    for c in s:
        p = c + p
    return p


# reverse(list(map(int, input().split())))
print(reverseString(input()))
