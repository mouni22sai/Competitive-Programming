class LinkedList:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createLinkedList(l):
    n = len(l)
    ll = LinkedList()

    for i in range(n):
        if ll.head is not None:
            p = ll.head
            ll.head = Node(l[n-i-1])
            ll.head.next = p
        else:
            ll.head = Node(l[n-i-1])

    return ll


def printList(ll):
    p = ll.head
    while p is not None:
        print(p.data)
        p = p.next


if __name__ == '__main__':
    l = list(map(int, input().split()))

    ll = createLinkedList(l)
    printList(ll)
