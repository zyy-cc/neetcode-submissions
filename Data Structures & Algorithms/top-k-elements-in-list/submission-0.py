class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # seen = {}
        # for val in nums:
        #     seen[val] = seen.get(val, 0) + 1
        # sorted_list = sorted(seen.items(), key = lambda item: item[1], reverse = True)
        # return [item[0] for item in sorted_list[:k]]
        seen = {}
        for val in nums:
            seen[val] = seen.get(val, 0) + 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in seen.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
        
        