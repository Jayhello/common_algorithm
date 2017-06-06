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


def heap_sort(seq):
    def adjust_heap(lst, beg, end):
        pivot = lst[beg]
        while 2 * beg + 1 < end:
            j = 2 * beg + 1
            if j + 1 < end and lst[j] < lst[j + 1]:
                j += 1

            if lst[j] > pivot:
                lst[beg] = lst[j]
                beg = j
            else:
                break

        lst[beg] = pivot

    LEN = len(seq)
    for i in xrange(LEN / 2 - 1, -1, -1):
        adjust_heap(seq, i, LEN)

    for i in xrange(LEN - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        adjust_heap(lst, 0, i - 1)

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    # lst = [3, -1, 5, 2, 11]
    lst = [3, -1, 5, 2, 11, 0, 9, 4, 7, -5, -2, 3]
    lst = [3, -1, 5, 2, 11, 101, -7, 7, 0, 9, 4, 7, -5, -2, 3]
    # insertion_sort(lst)
    # shell_sort(lst)
    heap_sort(lst)
    print lst
    # print insert_sort(lst)
    # for j in xrange(0, 5, -1):
    # for j in xrange(0, 5):
    #     print j
    # s = '\xe5\xbf\x85\xe6\xad\xbb'
    # s = '\xd0\xd3'
    # print s

    # for i in xrange(3, 0, -1):
    #     print i

    pass

