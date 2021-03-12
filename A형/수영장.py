from itertools import combinations


class Solution:

    def twoSum(self, nums, target):

        new_nums = []
        for i in range(len(nums)):

            if nums[i] <= target:
                new_nums.append([nums[i], i])

        check_list = []
        for i in range(len(new_nums), 0, -1):
            check_list.append(list(combinations(new_nums, i)))
        print(check_list)
        for i in check_list:
            print(i)
            for j in i:
                tmp = 0
                ans = []
                for k in j:
                    tmp += k[0]
                    ans.append(k[1])

                if tmp == target:
                    return ans

s = Solution()
print(s.twoSum([0,4,3,0], 0))