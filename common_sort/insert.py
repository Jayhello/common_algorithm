# _*_ coding:utf-8 _*_
"""
This file is about insert sort
"""


def insert_sort(lst):
    LEN = len(lst)

    for i in xrange(1, LEN):
        pivot = lst[i]
        k = 0  # note the scope question, if use j, not k you will get error
        for j in xrange(0, i):
            if pivot < lst[i - j - 1]:
                lst[i - j] = lst[i - j - 1]
                k += 1
            else:
                break
        # note the scope question
        if k != 0:
            lst[i - k] = pivot
    return lst
    pass


def insertion_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            j -= 1


def shell_sort(seq):
    """
    shell sort function
    :param seq:
    :return:
    """
    LEN = len(seq)

    jump = LEN  # step
    condition = True

    while condition:
        jump = (jump - 1) / 2 + 1
        for i in xrange(jump, LEN):
            j = i
            while j >= jump and seq[j - jump] > seq[j]:
                seq[j - jump], seq[j] = seq[j], seq[j - jump]
                j -= jump
        # emulate do while
        condition = True if jump > 1 else False

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    # lst = [3, -1, 5, 2, 11]
    lst = [3, -1, 5, 2, 11, 0, 9, 4, 7, -5, -2, 3]
    # insertion_sort(lst)
    shell_sort(lst)
    print lst
    # print insert_sort(lst)
    # for j in xrange(0, 5, -1):
    # for j in xrange(0, 5):
    #     print j

    pass

