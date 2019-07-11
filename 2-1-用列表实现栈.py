# -*- coding: utf-8 -*-


class MyStack:
    def __init__(self):
        self.items = []

        # 判断栈是否为空
    def isEmpty(self):
        return len(self.items) == 0

        # 返回栈的大小
    def size(self):
        return len(self.items)

        # 返回栈顶元素
    def top(self):
        if self.items:
            return self.items[-1]

    # 弹栈
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("栈已经为空")

    # 压栈
    def push(self, item):
        self.items.append(item)


if __name__ == "__main__":
    s = MyStack()
    for i in range(6):
        s.push(i)
    print(f"栈元素为：{s.items}")
    print(f"栈大小为：{s.size()}")
    print(f"栈顶元素为：{s.top()}")
    s.pop()
    print(f"弹出一个后，栈元素为：{s.items}")
