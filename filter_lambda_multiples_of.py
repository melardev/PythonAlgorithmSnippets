def get_multiples_of(max_value, multiples_of):
    return list(filter(lambda x: not x % multiples_of, range(max_value)))


# get multiples of 4, up to 80(not included)
print(get_multiples_of(80, 4))
