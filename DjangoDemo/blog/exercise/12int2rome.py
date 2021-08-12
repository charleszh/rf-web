class Solution(object):
    def int_2_rome(self, num):
        """

        :param num: int
        :return: str
        """
        special_rome_dict = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        common_rome_dict = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        M = num//1000*'M'
        C = num%1000//100
        if C == 9:
            C = 'CM'
        elif C == 4:
            C = 'CD'
        else:
            C = C//5*'D'
            C += C%5*C
        X = num%100//10
        if X == 9:
            X = 'XC'
        elif X == 4:
            X = 'XL'
        else:
            X = X//5*'L'
            X += X%5*'X'
        I = num%10
        if I == 9:
            I = 'IX'
        elif I == 4:
            I = 'IV'
        else:
            I = I//5*'V'
            I += I%5*'I'
        return M+C+X+I
    '''
    enumerate:
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    :return M[num//1000] + C[num%1000//100] + X[num%100//10] + I[num%10] 
    '''



if __name__ == '__main__':
    rome = Solution().int_2_rome(1994)
    print(rome)
