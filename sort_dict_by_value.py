'''
Snippet showing how to use sorted() builtin function to sort a dictionary by value
'''
social_media_links = {
    "Youtube": "https://youtube.com/Melardev",
    "Facebook": "https://facebook.com/Melardev",
    "Instagram": "https://instagram.com/melar_dev",
    "Twitter": "https://twitter.com/@melardev",
}

print('Original order')
for key in social_media_links:
    print('%s: %s' % (key, social_media_links[key]))

print()
print()

# sorted() may take a key arg which is a function to customize sorting
# by default sorting is done in ascending order, set reverse=True as arg for the opposite
print('Sorted')
for key, value in sorted(social_media_links.items(), key=lambda item: item[1], reverse=False):
    print("%s: %s" % (key, value))
