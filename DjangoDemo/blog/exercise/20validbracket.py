class Solution(object):
    def valid_bracket(self, s):
        brackets_dict = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for item in s:
            if item in brackets_dict:
                stack.append(item)
            else:
                if stack:
                    right_bracket = stack.pop()
                    if item != brackets_dict[right_bracket]:
                        return False
                else:
                    return False
        # if len(stack) == 0:
        #     return True
        # else:
        #     return False
        return not stack


if __name__ == '__main__':
    result = Solution().valid_bracket("([])")
    print(result)

