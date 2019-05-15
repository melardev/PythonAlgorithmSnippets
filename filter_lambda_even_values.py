def filter_even(iterable):
    return list(filter(lambda x: x % 2 != 0, iterable))


print(filter_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 21, 23, 44, 45, 46, 80, 85, 86, 87]))
