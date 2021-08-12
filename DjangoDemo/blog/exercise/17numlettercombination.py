class Solution(object):
    def num_letter_combination(self, nums):
        num_letter_dict = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        final_res = []
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return num_letter_dict[int(nums[0])]
        res = self.num_letter_combination(nums[1:])
        for i in res:
            for j in num_letter_dict[int(nums[0])]:
                final_res.append(i+j)
        return final_res


if __name__ == '__main__':
    num_letters = Solution().num_letter_combination('234')
    print(num_letters)
