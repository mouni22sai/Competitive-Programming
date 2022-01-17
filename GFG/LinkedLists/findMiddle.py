class LinkedList:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createLinkedListFromArray(l):
    ll = LinkedList()
    n = len(l)
    for i in range(n):
        if ll.head is not None:
            p = ll.head
            ll.head = Node(l[n - 1 - i])
            ll.head.next = p
        else:
            ll.head = Node(l[n - 1 - i])

    return ll


def printList(ll):
    p = ll.head
    while p is not None:
        print(p.data)
        p = p.next


def middleElement(ll):
    main_ptr = ll.head
    ref_ptr = ll.head

    if main_ptr is None:
        return -1
    if main_ptr.next is None:
        return main_ptr.data

    while main_ptr.next and main_ptr.next.next is not None:
        main_ptr = main_ptr.next.next
        ref_ptr = ref_ptr.next

    if main_ptr.next is not None and main_ptr.next.next is None:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next

    return ref_ptr.data


if __name__ == '__main__':
    l = list(map(int, input().split()))

    ll = createLinkedListFromArray(l)

    printList(ll)

    print(middleElement(ll))