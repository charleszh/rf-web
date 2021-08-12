class Solution(object):
    def get_longest_prefix(self, strs):
        """

        :param strs: list
        :return: str
        """
        if not strs:
            return ''
        sample = strs[0]
        for i in range(len(sample)):
            for s in strs[1:]:
                if i < len(s):
                    if sample[i] != s[i]:
                        return sample[:i]
                else:
                    return s[:i]
        return sample


if __name__ == '__main__':
    longest_str = Solution().get_longest_prefix(['st', 'str234', 'str1'])
    print(longest_str)

