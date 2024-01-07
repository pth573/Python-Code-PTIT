class Solution:
    def minOperations(self, nums) -> int:
        n = [0] * (len(nums) + 2)
        m = [0] * (len(nums) + 3)
        for i in range(2, len(nums) + 2):
            n[i] = n[i - 1] + 1 if nums[i - 2] == 'N' else n[i - 1]
        for i in range(1, len(nums) + 2):
            print(n[i], end=' ')
        
        # for i in range(len(nums), 1, -1):
        #     m[i] = m[i + 1] + 1 if nums[i - 2] == 'Y' else m[i + 1]
        # for i in range(len(nums) + 1, -1):
        #     print(n[i] + m[i])
    

customers = "YYNY"
s = Solution()
print(s.minOperations(customers))