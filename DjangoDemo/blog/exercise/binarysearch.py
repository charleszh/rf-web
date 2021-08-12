def binary_search(alist, target):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == target:
            return True
        else:
            if alist[midpoint] > target:
                return binary_search(alist[:midpoint], target)
            else:
                return binary_search(alist[midpoint+1:], target)

if __name__ == '__main__':
    a = binary_search([17, 20, 26, 31, 44, 54, 55, 65, 77, 93], 54)
    print(a)
