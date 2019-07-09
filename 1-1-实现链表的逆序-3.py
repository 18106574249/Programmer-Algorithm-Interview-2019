# -*- coding: utf-8 -*-

# 构造链表中的节点
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None


def  Reverse(head):
    if not head or not head.next:
        return head
    cur = head.next.next
    head.next.next = None
    while cur:
        post = cur.next
        cur.next = head.next
        head.next = cur
        cur = post


    return head



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

    head = Reverse(head)

    print("\n逆序后：")
    cur = head.next
    while cur != None:
        print(cur.item, end=" ")
        cur = cur.next
