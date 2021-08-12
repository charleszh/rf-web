class Solution(object):
    def nearest_sum_of_3_nums(self, num_list, target):
        """

        :param num_list: number list
        :param target: num
        :return: 3 nums whose sum is 0
        """
        num_list = sorted(num_list)
        res = num_list[0] + num_list[1] + num_list[2]
        for i in range(len(num_list)-2):
            left = i + 1
            right = len(num_list) - 1
            while left < right:
                c = num_list[i] + num_list[left] + num_list[right]
                if c == target:
                    return c
                if abs(res-target) > abs(c - target):
                    res = c
                if c > target:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == '__main__':
    sum = Solution().nearest_sum_of_3_nums([-1, 2, 1, -4], 1)
    print(sum)
