from queue import Queue
import random


class Stack:
    def __init__(self, size=float('inf')) -> None:
        self.l = []
        self.size = 0
        self.limit = size

    def pop(self):
        if self.IsEmpty():
            print("UnderFlow")
        self.size -= 1
        return self.l.pop()

    def push(self, value):
        if self.size == self.limit:
            print("OverFlow")
            return
        self.size += 1
        self.l.append(value)

    def __repr__(self) -> str:
        return f"{self.l}"

    def IsEmpty(self) -> bool:
        return not self.size

    def size(self) -> int:
        return self.size


class queue:
    def __init__(self, size=float('inf')) -> None:
        self.l = []
        self.size = 0
        self.limit = size

    def dequeue(self):
        if self.IsEmpty():
            print("UnderFlow")
        self.size -= 1
        return self.l.pop(0)

    def enqueue(self, value):
        if self.size == self.limit:
            print("OverFlow")
            return
        self.size += 1
        self.l.append(value)

    def __repr__(self) -> str:
        return f"{self.l}"

    def IsEmpty(self) -> bool:
        return not self.size

    def size(self) -> int:
        return self.size


class deque(queue):

    def popleft(self):
        if super().IsEmpty():
            print("UnderFlow")
        self.size -= 1
        return self.l.pop()


q = deque(size=10)
for i in range(11):
    q.enqueue(random.random())
    print(q)
print([q.popleft() for i in range(5)])
