# 单调队列
import queue

class MaxQueue:

    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        while self.deque and value > self.deque[-1]:
            self.deque.pop()
        self.queue.put(value)
        self.deque.append(value)

    def pop_front(self) -> int:
        if self.queue.empty():
            return -1
        temp = self.queue.get()
        if self.deque[0] == temp:
            self.deque.popleft()
        return temp


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

a = MaxQueue()
a.push_back(1)
a.push_back(5)
a.push_back(2)
a.push_back(4)