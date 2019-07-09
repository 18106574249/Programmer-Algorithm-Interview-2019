# -*- coding: utf-8 -*-

# 构造链表中的节点
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

# 通过增加额外的列表存放链表节点值，用于空间换时间。
def  RemoveDuplicate(head):
    if  head == None or head.next == None:
        return

    # 全部链表节点值
    all_items = []

    # 判断有无重复并删除节点
    pre = head
    cur = head.next
    while cur != None:
        post = cur.next
        # print(cur.item)
        if cur.item in all_items:
            pre.next = post.next
            pre = post
            cur = post.next
        else:
            all_items.append(cur.item)
            pre = cur
            cur = post



if  __name__=="__main__":
    # 构造单链表
    head = Node()
    cur = head
    for i in [1, 2,3,1,3]:
        cur.next = Node(i)
        cur = cur.next

    print("删除重复节点前：")
    cur = head.next
    while cur != None:
        print(cur.item, end=" ")
        cur = cur.next

    RemoveDuplicate(head)

    print("\n删除重复节点后：")
    cur = head.next
    while cur != None:
        print(cur.item, end=" ")
        cur = cur.next
