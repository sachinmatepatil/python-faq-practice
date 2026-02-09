import random



def gen_ran_alpNum_str(l):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    if l>6:
        return ''.join(random.choice(chars) for ch in range(l))

words=10
print(gen_ran_alpNum_str(words))