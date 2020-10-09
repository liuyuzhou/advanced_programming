def dedupe_1(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


sequence_v = [1, 2, 3, 5, 2, 3]
print(list(dedupe_1(sequence_v)))


def dedupe_2(items, key=None):
    seen = set()
    for item in items:
        # val = item if key is None else key(item)
        if (val := item if key is None else key(item)) not in seen:
            yield item
            seen.add(val)

sequence_v = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe_2(sequence_v, key=lambda d: (d['x'],d['y']))))
print(list(dedupe_2(sequence_v, key=lambda d: d['x'])))
