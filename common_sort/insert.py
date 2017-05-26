# _*_ coding:utf-8 _*_
"""
This file is about insert sort
"""


def insert_sort(lst):
    LEN = len(lst)

    for i in xrange(1, LEN):
        pivot = lst[i]
        k = 0
        for j in xrange(0, i):
            if pivot < lst[i - j - 1]:
                lst[i - j] = lst[i - j - 1]
                k += 1
            else:
                break
        print 'k: ', k
        if k != 0:
            lst[i - k] = pivot
    return lst
    pass

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    lst = [3, -1, 5, 2, 11]
    lst = [3, -1, 5, 2, 11, 0, 9, 4]
    print insert_sort(lst)
    # for j in xrange(0, 5, -1):
    # for j in xrange(0, 5):
    #     print j

    pass
