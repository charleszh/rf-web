class Solution(object):
    def sum_of_3_nums(self, num_list):
        """

        :param num_list: number list
        :return: 3 nums whose sum is 0
        """
        num_list = sorted(num_list)
        res = []
        for i in range(len(num_list)-2):
            left = i + 1
            right = len(num_list) - 1
            if i > 0 and num_list[i] == num_list[i-1]:
                continue

            while left < right:
                c = num_list[i] + num_list[left] + num_list[right]
                if c == 0:
                    res.append([num_list[i], num_list[left], num_list[right]])
                    while num_list[right] == num_list[right-1] and right > left:
                        right -= 1
                    while num_list[left] == num_list[left+1] and right > left:
                        left += 1

                    left += 1
                    right -= 1
                elif c > 0:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == '__main__':
    sum = Solution().sum_of_3_nums([-1, 0, 1, 2, -1, -4])
    print(sum)
