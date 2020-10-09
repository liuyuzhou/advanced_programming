class Item:
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    # queue_1 = Item('queue_1')
    # queue_2 = Item('queue_2')
    # print(queue_1 < queue_2)

    # queue_1 = (1, Item('queue_1'))
    # queue_2 = (3, Item('queue_2'))
    # queue_3 = (1, Item('queue_3'))
    # print(queue_1 < queue_2)
    # print(queue_1 < queue_3)

    queue_1 = (1, 0, Item('queue_1'))
    queue_2 = (3, 1, Item('queue_2'))
    queue_3 = (1, 2, Item('queue_3'))
    print(queue_1 < queue_2)
    print(queue_1 < queue_3)

