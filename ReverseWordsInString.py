string_input=input('Enter string')

#MEthod 1
r_w_s=string_input.split()
r_w_s.reverse()
resul=' '.join(r_w_s)
print(resul)

#MEthod 2
# temp = string_input.split()
# result=temp[-1::-1]
# final=' '.join(result)
# print(final)

s = "sachin subhash mate"

#Method 3
def rev_s(s):
    rev_s = ''

    word_list = s.split()

    for word in word_list:
        rev_s = word + ' ' + rev_s

    return rev_s


print(rev_s(s))