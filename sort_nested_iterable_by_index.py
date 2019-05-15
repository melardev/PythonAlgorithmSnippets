"""
We will sort a list of tuples based on the index of a tuple that is contained in the list
This would also work for list of lists (shown in other demo)
"""


def sort_callback(value):
    return value[1]


my_list_of_tuples = [(1, 2), (2, 3), (3, 4), (2, 2), (2, 1)]

my_list_of_tuples.sort(key=sort_callback)
print(my_list_of_tuples)

my_list_of_tuples.sort(key=sort_callback, reverse=True)
print(my_list_of_tuples)
