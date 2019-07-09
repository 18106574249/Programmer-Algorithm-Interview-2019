# -*- coding: utf-8 -*-

# 构造链表中的节点
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None


def Reverse(head):
    # 判断链表是否为空
    if head == None or head.next == None:
        return

    pre = None          # 前驱结点
    post = None         # 后继结点
    cur = head.next     # 当前结点

    while cur.next:
        post = cur.next
        cur.next = pre
        pre = cur
        cur = post

    cur.next = pre
    head.next = cur


if __name__ == "__main__":
    # 构造单链表
    head = Node()
    cur = head
    for i in range(1, 10):
        cur.next = Node(i)
        cur = cur.next

    print("逆序前：")
    cur = head.next
    while cur != None:
        print(cur.item, end=" ")
        cur = cur.next

    Reverse(head)

    print("\n逆序后：")
    cur = head.next
    while cur != None:
        print(cur.item, end=" ")
        cur = cur.next
