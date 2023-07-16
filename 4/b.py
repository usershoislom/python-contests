import heapq

def merge_sorter(*sequences):
    heap = []
    for i, seq in enumerate(sequences):
        iterator = iter(seq)
        item = next(iterator, None)
        if item is not None:
            heapq.heappush(heap, (item, i, iterator))

    while heap:
        item, i, iterator = heapq.heappop(heap)
        yield item
        next_item = next(iterator, None)
        if next_item is not None:
            heapq.heappush(heap, (next_item, i, iterator))
# a = [1, 3, 5, 7, 9]
# b = [2, 4, 6, 8, 10]
# c = merge_sorter(a, b)
# for item in c:
#     print(item)
