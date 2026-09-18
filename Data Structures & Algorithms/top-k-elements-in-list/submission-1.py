class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # seen = {}
        # for val in nums:
        #     seen[val] = seen.get(val, 0) + 1
        # sorted_list = sorted(seen.items(), key = lambda item: item[1], reverse = True)
        # return [item[0] for item in sorted_list[:k]]
        
        # count frequency
        seen = {}
        for val in nums:
            seen[val] = seen.get(val, 0) + 1
        
        # convert frequency to bucket frequency to [nums], avoid sorting
        bucket = [[] for _ in range(len(nums) + 1)]
        for val, freq in seen.items():
            bucket[freq].append(val)
        
        res = []
        for i in range(len(nums), -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res


        
        