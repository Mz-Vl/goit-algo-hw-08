import heapq


def connect(cables):
    heap = []
    for c in cables:
        heapq.heappush(heap, c)

    total_cost = 0
    while len(heap) > 1:
        cost1 = heapq.heappop(heap)
        cost2 = heapq.heappop(heap)
        total_cost += cost1 + cost2
        heapq.heappush(heap, cost1 + cost2)

    return total_cost


cables = [1, 2, 4, 10]
print(connect(cables))
