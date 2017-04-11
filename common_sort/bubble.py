# _*_ coding:utf-8 _*_


def ret_swap(v1, v2):
    return v2, v1


def bubble_sort(lst):
    LEN = len(lst)
    for i in range(1, LEN):
        for j in range(i, LEN):
            if lst[-j] < lst[-j-1]:
                lst[-j], lst[-j-1] = ret_swap(lst[-j], lst[-j-1])

    return lst
    pass

if __name__ == '__main__':
    lst = [3, 9, 6]
    print bubble_sort(lst)

    pass
