class Solution(object):
    def is_palindrome(self, num):
        """

        :param num: int
        :return: bool
        """
        s = str(num)
        return s == s[::-1]

    def my_reverse(self, s):
        return s[::-1]

    def my_reverse2(self, s):
        return ''.join(reversed(s))

    def my_reverse3(self, s):
        if s == '':
            return s
        else:
            return self.my_reverse3(s[1:]) + s[0]

    def my_reverse4(self, s):
        s_list = list(s)
        r_list = s_list.reverse()
        return ''.join(r_list)

if __name__ == "__main__":
    new_s = Solution().is_palindrome("abcdba")
    print(new_s)
