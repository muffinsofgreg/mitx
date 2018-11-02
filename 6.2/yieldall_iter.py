def powerset(items):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(items) <= 0:
        yield []
    else:
        for item in powerset(items[1:]):
            yield [items[0]] + item
            yield item


items = ["bucket", "driver", "mouse", "hatchet", "gourd", "bottle"]

new = powerset(items)

for item in new:
    print(item)
