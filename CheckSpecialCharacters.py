import re

str = "Welcome@@ google## here is best %%"

regex=re.compile(("[!@#$%^&*(]"))

if(regex.search(str)==None):
    print('no special char')
else:
    print('string contains special character')