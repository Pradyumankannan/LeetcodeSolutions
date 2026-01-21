class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        for i, num in enumerate( nums ):
            # we have to do OR operation on a , a + 1
            # a = xxxxxxx0 ending with 0
            # a + 1 = xxxxxxx1
            # a = xxxxxxxx1 ending with 1 
            # a = xxxxxxx10 
            # Prime numbers so they will always be odd

            # lets see cases
            # 2 = -1 
            # 3 = 11 -> 10 | 01
            # 5 = 101 -> 100 | 101
            # 7 = 111 -> 11 | 100
            # 11 = 1011 -> 1001 | 1010

            # trailing ones getting shifted 

            res = -1
            d = 1
            while (nums[i] & d) != 0:
                res = nums[i] - d
                d <<= 1
            ans[i] = res
        return ans 
