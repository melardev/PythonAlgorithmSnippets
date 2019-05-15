'''
Snippet showing how to use sorted() builtin function to sort a dictionary by key
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

print('Sorted')
for key in sorted(social_media_links.keys()):
    print("%s: %s" % (key, social_media_links[key]))
