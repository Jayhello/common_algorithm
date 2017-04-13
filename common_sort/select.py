# _*_ coding:utf-8 _*_
from common_utils.com_algorithm import ret_swap


def select_sort(lst):
    LEN = len(lst)
    for i in xrange(LEN - 1):
        idx_min = i
        for j in xrange(i, LEN):
            if lst[idx_min] > lst[j]:
                # there is no need to swap value, just get the index
                idx_min = j

        if idx_min != i:
            lst[i], lst[idx_min] = ret_swap(lst[i], lst[idx_min])

    return lst
    pass


if __name__ == '__main__':
    lst = [3, -1, 5, 2, 11]
    print select_sort(lst)
    pass
