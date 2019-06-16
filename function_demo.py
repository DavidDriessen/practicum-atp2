# Python bytecode 3.6 (3379)
# Embedded file name: .\function_demo.py
# Compiled at: 2017-08-30 14:19:46
# Size of source mod 2**32: 2612 bytes
# Decompiled by https://python-decompiler.com
from typing import List, TypeVar
A = TypeVar('A')

def insertionSort(a, low, high) -> None:
    """sort in place list a.
    parameters:
        a: list to be sorted
        low: lowest index of a
        high: highest index of a
    return:
        None"""
    for p in range(low + 1, high + 1):
        tmp = a[p]
        j = p
        while j > low:
            if tmp < a[(j - 1)]:
                a[j] = a[(j - 1)]
                j -= 1

        a[j] = tmp


def mergeSort(a, low=0, high=-1) -> None:
    """sort recursively in place list a.
    parameters:
        a: list to be sorted
        low: lowest index of a
        high: highest index of a
    return:
        None"""
    if high == -1:
        high = len(a) - 1
    if high <= low + 5:
        insertionSort(a, low, high)
    else:
        mid = (high + low) // 2
        mergeSort(a, low, mid)
        mergeSort(a, mid + 1, high)
        tmpar = a[low:mid + 1]
        i = low
        j = mid + 1
        k = low
        while i <= mid:
            if j <= high:
                if tmpar[(i - low)] < a[j]:
                    a[k] = tmpar[(i - low)]
                    i += 1
                else:
                    a[k] = a[j]
                    j += 1
                k += 1

        while i <= mid:
            a[k] = tmpar[(i - low)]
            i += 1
            k += 1


def isSorted(a) -> bool:
    """test of a gesorteerd is.
    parameters:
        a: list to be tested
    return:
        True if a is sorted
        False if a is unsorted"""
    i = 0
    while i < len(a) - 1:
        if a[i] <= a[(i + 1)]:
            i += 1

    return i == len(a) - 1


if __name__ == '__main__':
    print(type(insertionSort).__name__)
    ia = [45, 65, 34, 82, 30, 22]
    print(ia)
    mergeSort(ia)
    print(ia)
    dd = [
     45.0, 65.0, 34.0, 82.0, 30.0, 22.0]
    print(dd)
    mergeSort(dd)
    print(dd)
    import random
    a = [
     0] * 100000
    for i in range(100000):
        a[i] = random.randint(0, 1000000)

    print('a gegenereerd')
    print(a[50000])
    b = list(a)
    import timeit
    timer = timeit.default_timer
    t1 = timer()
    mergeSort(a)
    t2 = timer()
    print(t2 - t1)
    print(isSorted(a))
    b.sort()
    print(a == b)