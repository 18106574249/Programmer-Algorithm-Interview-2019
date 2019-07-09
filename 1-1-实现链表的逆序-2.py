# -*- coding: utf-8 -*-

# 构造链表中的节点
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None


def  RecursiveReverse(head):
    if not head or not head.next:
        return head
    # 找到最后一个节点作为新的 head
    newhead=RecursiveReverse(head.next)
    # 当前节点后的节点指向当前节点，本节点指向None（防止互相指向）
    head.next.next=head
    head.next=None
    return  newhead


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


    head = RecursiveReverse(head.next)

    print("\n逆序后：")
    cur = head
    while cur != None:
        print(cur.item, end=" ")
        cur = cur.next
