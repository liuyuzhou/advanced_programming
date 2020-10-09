# 优先级队列
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == "__main__":
    priority_queue = PriorityQueue()
    priority_queue.push(Item('queue_1'), 1)
    priority_queue.push(Item('queue_2'), 3)
    priority_queue.push(Item('queue_3'), 5)
    priority_queue.push(Item('queue_4'), 3)

    print(priority_queue.__dict__.get('_queue')[0])
    print(f'pop item is:{priority_queue.pop()}')

    print(priority_queue.__dict__.get('_queue')[0])
    print(f'pop item is:{priority_queue.pop()}')

    print(priority_queue.__dict__.get('_queue')[0])
    print(f'pop item is:{priority_queue.pop()}')

    print(priority_queue.__dict__.get('_queue')[0])
    print(f'pop item is:{priority_queue.pop()}')

    print(priority_queue.__dict__)
