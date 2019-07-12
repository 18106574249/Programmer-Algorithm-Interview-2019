# -*- coding: utf-8 -*-


class Stack:

    # 模拟栈
    def __init__(self):
        self.items = []

    # 判断栈是否为空
    def empty(self):
        return len(self.items) == 0

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 返回栈顶元素
    def peek(self):
        if not self.empty():
            return self.items[len(self.items) - 1]
        else:
            return None

    # 弹栈
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("栈已经为空")

    # 压栈
    def push(self, item):
        self.items.append(item)


def moveBottomToTop(s):
    if s.empty():
        return
    top1 = s.peek()
    s.pop()          # 弹出栈顶元素
    if not s.empty():
        # 递归处理不包含栈顶元素的子栈
        moveBottomToTop(s)
        top2 = s.peek()
        s.pop()
        # 交换栈顶元素与子栈栈顶元素 
        s.push(top1)
        s.push(top2)
    else:
        s.push(top1)


def reverse_stack(s):
    if s.empty():
        return
        # 把栈底元素移动到栈顶
    print(f"1: {s.items}")
    moveBottomToTop(s)
    print(f"2: {s.items}")

    top = s.peek()
    s.pop()
    # 递归处理子栈
    reverse_stack(s)
    s.push(top)


if __name__ == "__main__":
    s = Stack()
    for i in range(6):
        s.push(i)
    print(f"翻转前栈的情况: {s.items}")
    reverse_stack(s)
    print(f"翻转后栈的情况: {s.items}")

