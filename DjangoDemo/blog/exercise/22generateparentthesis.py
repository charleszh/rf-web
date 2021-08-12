class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generator(left, right, s, res):
            if left<0 or right<0 or left>right:
                return
            if left==0 and right==0:
                res.append(s)

            generator(left-1, right, s+'(', res)
            generator(left, right-1, s+')', res)

        res = []
        generator(n, n, '', res)
        return res


if __name__ == '__main__':
    result = Solution().generateParenthesis(3)
    print(result)
