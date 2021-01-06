# https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3594/

class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        counter = 0
        for i, n in enumerate(arr):
            if i == 0:
                counter += n - 1
            else:
                counter += n - arr[i-1] - 1
            
            if counter >= k:
                return n - (counter - k) - 1
        
        if counter < k:
            return arr[-1] + (k - counter)



if __name__ == "__main__":
    arr = [1,2,3,4]
    k = 2
    s = Solution()
    print(s.findKthPositive(arr, k))