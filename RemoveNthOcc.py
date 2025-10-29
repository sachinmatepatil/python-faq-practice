#Problem - Remove the Nth occurence of the given word

lst = ['geeks','for','geeks']
word = 'geeks'
n=2

count=0
for i in range(0,len(lst)):
    if lst[i]==word:
        count=count+1
    if count==n:
        # del lst[i]
        # or
        lst.pop(i)
print(lst)

