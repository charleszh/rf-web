class Solution(object):
    def get_most_water(self, height):
        """

        :param height: list
        :return: num
        """
        start = 0
        end = len(height) - 1
        max_v = 0
        while start < end:
            max_v = max(max_v, min(height[start], height[end]) * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_v


if __name__ == "__main__":
    most_water = Solution().get_most_water([4,3,2,20,5])
    print(most_water)
