class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        # use hash map to store each element

        anagram = {}

        for val in strs:
            initial = "".join(sorted(val))
            if initial not in anagram:
                anagram[initial] = [val]
            else:
                anagram[initial].append(val)
        return list(anagram.values())



       
      
       

            





        


        