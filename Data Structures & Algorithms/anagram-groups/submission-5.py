class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        # use hash map to store each element， sorting will use O(nlongn)
        # anagram = {}

        # for val in strs:
        #     initial = "".join(sorted(val))
        #     if initial not in anagram:
        #         anagram[initial] = [val]
        #     else:
        #         anagram[initial].append(val)
        # return list(anagram.values())

        anagram = {}
        for val in strs:
            count = [0] * 26
            for char in val:
                index = ord(char) - ord("a")
                count[index] += 1
            key = tuple(count)
            if key not in anagram:
                anagram[key] = []
            anagram[key].append(val)
        return list(anagram.values())





       
      
       

            





        


        