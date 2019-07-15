# -*- coding: utf-8 -*-

from collections import deque


class LRU:
    def __init__(self, cacheSize):
        self.cacheSize = cacheSize
        self.queue = deque()
        self.Set = set()

    def isQueueFull(self):
        return len(self.queue) == self.cacheSize

    def enqueue(self, pageNum):

        if self.isQueueFull():
            self.Set.remove(self.queue[-1])
            self.queue.pop()
        self.queue.appendleft(pageNum)
        self.Set.add(pageNum)

    def accessPage(self, pageNum):
        # page不在缓存队列中，把它缓存到队首
        if pageNum not in self.Set:
            self.enqueue(pageNum)
        # page已经在缓存队列中了，移动到队首
        elif pageNum != self.queue[0]:
            self.queue.remove(pageNum)
            self.queue.appendleft(pageNum)

    def printQueue(self):
        while len(self.queue) > 0:
            print(self.queue.popleft()),


if __name__ == "__main__":
    # 假设缓存大小为3
    lru = LRU(3)
    # 访问page 
    lru.accessPage(1)
    lru.accessPage(2)
    lru.accessPage(5)
    lru.accessPage(1)
    lru.accessPage(6)
    lru.accessPage(7)
    # 通过上面的访问序列后，缓存的信息为
    lru.printQueue()
