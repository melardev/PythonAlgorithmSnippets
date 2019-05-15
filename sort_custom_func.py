# Accumulate the even numbers in one side, the odd numbers in the other side
def sort_callback(value):
    return value % 2 == 0


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Sort in ascending order based on the sort_callback
my_list.sort(key=sort_callback)
print(my_list)

# Sort in descending order based on the sort_callback
my_list.sort(key=sort_callback, reverse=True)
print(my_list)
