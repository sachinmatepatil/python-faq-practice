s='welcome to python programming'


#Method 1
# listss=s.split()
#
# sun_s='python'
# for i in listss:
#     if sun_s==i:
#         print('Subs present')

#MEthod 2
sub_s='python'
if s.find(sub_s)==-1:
    print('not found')
else:
    print('found')

s = 'welcome to python programming'
v = 'python'
def find_sub(s, v):
    words = s.split()

    for word in words:
        if word == v:
            return True
    return False


print(find_sub(s, v))