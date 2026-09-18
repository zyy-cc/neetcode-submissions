class Solution:

    def encode(self, strs: List[str]) -> str:
        length_list = [str(len(val)) for val in strs]
        encoded_string = ""
        for i in range(len(strs)):
            encoded_string += length_list[i] + "," + strs[i]
        return encoded_string
         

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        while start < len(s):
            # find comma
            comma_index = s.find(",", start)
            # find the length
            length = int(s[start:comma_index])
            res.append(s[comma_index + 1 : comma_index + 1 + length])
            start = comma_index + 1 + length
        return res
        
             


        
