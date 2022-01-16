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


def searchInList(ll, x):

    p = ll.head

    while p is not None:
        if p.data == x:
            return True
        p = p.next
    return False


def returnNodeAtGivenIndexBase1(ll, k):

    i = 1
    p = ll.head
    while i < k:
        p = p.next
        i = i + 1
    return p.data
        

if __name__ == '__main__':
    l = list(map(int, input().split()))

    # Create Linked List from input array
    ll = createLinkedList(l)

    # Print the created linked list
    printList(ll)

    # Search if the entered element exists in the created linked list
    print(searchInList(ll, int(input('Enter a number to check its presence : '))))

    # Print node at a given index in the created linked list
    print(returnNodeAtGivenIndexBase1(ll, int(input('Find nth node in the linked list, Enter n: '))))
