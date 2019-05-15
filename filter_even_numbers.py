def filter_multiples_of(n):
    return n % 2 == 0


def get_multiples_of(max_value):
    return list(filter(filter_multiples_of, range(max_value)))


# Get even numbers
print(get_multiples_of(80))
