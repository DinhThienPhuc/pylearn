import re

txt = 'The rain in Spain'
is_included = re.search('^The.*Spain$', txt)
print(is_included.start())

get_text = re.findall('ai', txt)
print(get_text)

no_match = re.findall('ahihi', txt)
print(no_match)

arr = re.split(r'\s', txt)
print(arr)

arr2 = re.split(r'\s', txt, 1)
print(arr2)
