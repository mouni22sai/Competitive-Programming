import io
import sys


class LinkedList:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


l = list(map(int, input().split()))

ll = LinkedList()
