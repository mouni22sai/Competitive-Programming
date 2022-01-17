class LinkedList:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createList(l):
    ll = LinkedList()
    n = len(l)
    for i in range(n):
        if ll.head:
            p = ll.head
            ll.head = Node(l[n-1-i])
            ll.head.next = p
        else:
            ll.head = Node(l[n-1-i])

    return ll


def printlist(ll):
    p = ll.head
    while p is not None:
        print(p.data)
        p = p.next


def countOccurances(ll, x):
    count = 0
    p = ll.head
    while p is not None:
        if p.data == x:
            count = count + 1
        p = p.next

    return count


if __name__ == '__main__':
    l = list(map(int, input().split()))

    ll = createList(l)

    printlist(ll)

    print(countOccurances(ll, int(input('Enter the element you want to find the number of occurances:'))))

