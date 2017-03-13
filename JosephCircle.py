class Node:
    def __init__(self, data):
        self.data = data
        self.next = self


class CLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
        self.head = new_node


def diners(head, k):
    current = head
    count = 0
    while current.next != head:
        if count == (k - 1):
            next = current.next
            current.next = next.next
            next = None
            count = 0
        else:
            count += 1
        current = current.next
    return current.data


if __name__ == '__main__':
    cll = CLinkedList()
    print("Enter circular linked list size")
    N = int(raw_input())
    print("Enter {} data".format(N))
    while N:
        data = int(raw_input())
        cll.push(data)
        N -= 1
    M = int(raw_input())
    print(diners(cll.head, M))
