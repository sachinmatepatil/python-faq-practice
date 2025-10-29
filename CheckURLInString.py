import re

str = 'her is my website https://sachinmatepatil.com/'

urlss=re.findall(("^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$+",str))

print(urlss)