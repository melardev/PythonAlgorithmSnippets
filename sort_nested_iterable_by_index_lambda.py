"""
We will sort a list of tuples based on the index of a list that is contained in the list
This would also work for list of tuples (shown in other demo)
"""


def sort_callback(value):
    return value[1]


my_list_of_tuples = [[1, 2], [2, 3], [3, 4], [2, 2], [2, 1]]

my_list_of_tuples.sort(key=lambda x: x[1])
print(my_list_of_tuples)

my_list_of_tuples.sort(key=lambda x: x[1], reverse=True)
print(my_list_of_tuples)
