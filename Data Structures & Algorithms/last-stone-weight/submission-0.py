class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [- ele for ele in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            larger = - heapq.heappop(heap)
            smaller = - heapq.heappop(heap)

            if smaller < larger:
                diff = larger - smaller
                heapq.heappush(heap, -diff)
        return -heap[0] if len(heap) == 1 else 0

        