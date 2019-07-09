# -*- coding: utf-8 -*-

# 构造链表中的节点
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

"""
** 方法功能：对带头结点的无序单链表删除重复的结点 
** 输入参数：head:链表头结点
"""
def  RemoveDuplicate(head):
    if  head == None or head.next == None:
        return
    outerCur = head.next  # 用于外层循环，指向链表第一个结点
    while  outerCur != None:
        innerCur = outerCur.next    # 用于内层循环用来遍历outerCur后面的结点
        innerPre = outerCur         # innerCur的前驱结点
        while  innerCur != None:
            # 找到重复的结点并删除
            if  outerCur.item == innerCur.item:
                innerPre.next = innerCur.next
                innerCur = innerCur.next
            else:
                innerPre = innerCur
                innerCur = innerCur.next
        outerCur = outerCur.next

if  __name__=="__main__":
    # 构造单链表
    head = Node()
    cur = head
    for i in [1, 2,3,1,3,7,5,9,11]:
        cur.next = Node(i)
        cur = cur.next

    print("删除重复节点前：")
    cur = head.next
    while cur != None:
        print(cur.item, end=" ")
        cur = cur.next

    removeDup(head)

    print("\n删除重复节点后：")
    cur = head.next
    while cur != None:
        print(cur.item, end=" ")
        cur = cur.next
