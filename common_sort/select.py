# _*_ coding:utf-8 _*_
from common_utils.com_algorithm import ret_swap


def select_sort(lst):
    LEN = len(lst)
    for i in xrange(LEN - 1):
        for j in xrange(i, LEN):
            if lst[i] > lst[j]:
                lst[i], lst[j] = ret_swap(lst[i], lst[j])

    return lst
    pass


if __name__ == '__main__':
    lst = [3, -1, 5, 2, 11]
    print select_sort(lst)
    pass
