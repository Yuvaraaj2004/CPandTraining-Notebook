from heapq import heappop, heappush
Algorithm A*(Source, Destination):
    heap = [[time, 0, Source, []]]
    ans = []
    while heap:
        time, distance, cur, trains = heappop(heap)
        if cur == Destination:
            ans.append(trains)
        else:
            for adjNode in adjacentNodes[cur]:
                heappush(heap, [new_time, newDistance,
                         adj_node, trains+[cur_train]])
    return ans
