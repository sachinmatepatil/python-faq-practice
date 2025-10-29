string_input=input('Enter string')

#MEthod 1
# r_w_s=string_input.split()
# r_w_s.reverse()
# resul=' '.join(r_w_s)
# print(resul)

#MEthod 2
temp = string_input.split()
result=temp[-1::-1]
final=' '.join(result)
print(final)