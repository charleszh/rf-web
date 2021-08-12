class Solution(object):
    def sum_4_nums(self, nums, target):
        """

        :param nums: int list
        :return: list which sum is target(0)
        """
        nums = sorted(nums)
        res = []
        len_nums = len(nums)
        for i in range(0, len_nums-3):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len_nums-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                start = j + 1
                end = len_nums - 1
                while start < end:
                    sum = nums[i] + nums[j] + nums[start] + nums[end]
                    if sum == target:
                        res.append([nums[i], nums[j], nums[start], nums[end]])
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        start += 1
                        end -= 1
                    elif sum > target:
                        end -= 1
                    else:
                        start += 1
        return res


if __name__ == '__main__':
    sum_list = Solution().sum_4_nums([1, 0, -1, 0, -2, 2], 0)
    print(sum_list)
