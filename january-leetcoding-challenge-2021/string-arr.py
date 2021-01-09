# https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3597/

class Solution:
    def arrayStringsAreEqual(self, word1: list, word2: list) -> bool:
        res_word_1 = ""
        res_word_2 = ""
        for w in word1:
            res_word_1 += w
        for w in word2:
            res_word_2 += w
        
        return res_word_2 == res_word_1

if __name__ == "__main__":
    s = Solution()
    print(s.arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"]))
    print(s.arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))