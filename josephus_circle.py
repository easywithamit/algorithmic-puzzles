#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: Amit Kumar
@mail: haywithamit@gmail.com
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def josephus_circle(head, M):
    if head is None:
        return None
    if head.next is None:
        return head.data
    counter = 1
    while head != head.next:
        if counter == M-1:
            head.next = head.next.next
            counter = 1
        else:
            counter += 1
            head = head.next
    return head.data


if __name__=='__main__':
    N = int(raw_input())
    ll = LinkedList()
    last_node = next = ll.head
    for i in xrange(N):
        d = int(raw_input())
        node = Node(d)
        if not last_node:
            last_node = node
        node.next = next
        next = node
    ll.head = next
    last_node.next = ll.head
    M = int(raw_input())
    print("The leader of the pack is {}".format(josephus_circle(ll.head, M)))
