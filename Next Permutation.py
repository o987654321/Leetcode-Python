from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1️⃣ 從後往前找「第一個下降點」
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2️⃣ 如果找到了下降點
        if i >= 0:
            # 從後面找比 nums[i] 大的「最小」值
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 交換 i, j
            nums[i], nums[j] = nums[j], nums[i]

        # 3️⃣ 將 i 後面的區間反轉
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
