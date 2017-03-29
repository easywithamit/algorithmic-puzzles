from random import randint


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.counter = 0

    def push(self, data):
        node = Node(data)
        self.counter += 1
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        val = randint(1, self.counter)
        state = 1
        current = self.head
        while current is not None:
            if state == val:
                self.head.random = current
            state += 1
            current = current.next

    def display(self, pattern='next'):
        if pattern == 'next' or pattern == 'random':
            current = self.head
            while current is not None:
                print(current.data, "->", current.random.data)
                # current = getattr(current,pattern)
                current = current.next
        else:
            print("Only two patterns available: next and random")


def clone_list(head):
    if head is None:
        return None
    else:
        current = head
        while current is not None:
            node = Node(current.data)
            node.next = current.random
            current.random = node
            current = current.next
        current = head
        while current is not None:
            node = current.random
            node.random = node.next.random
            if current.next:
                node.next = current.next.random
            else:
                node.next = None
            current = current.next
        return head.random


if __name__ == '__main__':
    ll = LinkedList()
    n = int(raw_input())
    while n:
        d = int(raw_input())
        ll.push(d)
        n -= 1
    print("Display by next")
    ll.display()
    # print("Display by random")
    # ll.display('random')
    ll2 = LinkedList()
    ll2.head = clone_list(ll.head)
    print("Display 2 by next")
    ll2.display()
# print("Display 2 by random")
# ll2.display('random')
