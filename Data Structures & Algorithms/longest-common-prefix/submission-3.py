class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        index = 0
        
        if len(strs[0]) > index:
            char = strs[0][index]

        while True:
            for word in strs:
                if index == len(word) or word[index] != char:
                    return ans

            ans += char
            index += 1

            if len(strs[0]) > index:
                char = strs[0][index]
