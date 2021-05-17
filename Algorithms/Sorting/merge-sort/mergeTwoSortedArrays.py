# merge two sorted arrays

def mergeTwoSortedLists(r, s):
    l = []
    lenR = len(r)
    lenS = len(s)
    i = 0  # first index of array r
    j = 0  # first index of array s

    for k in range(lenR+lenS):
        if i <= lenR-1 and j <= lenS-1:
            if r[i] <= s[j]:
                l.append(r[i])
                i = i + 1
            if r[i] > s[j]:
                l.append(s[j])
                j = j + 1
        elif i >= lenR and j <= lenS-1:
            l.append(s[j])
            j = j+1
        elif j >= lenS and i <= lenR-1:
            l.append(r[i])
            i = i+1
        k = k+1
    return l


print(mergeTwoSortedLists(list(map(int, input().split())), list(map(int, input().split()))))

# Time taken by this = Theta(lenR+lenS)
# Space complexity of this is Theta(lenR + lenS)
# Can get O(1) space complexity by just printing the elements and not appending them to the auxiliary array
