def short_bubble_sort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                exchanges = True

        passnum= passnum - 1
    return alist

if __name__ == '__main__':
    new_list = short_bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
    print(new_list)
