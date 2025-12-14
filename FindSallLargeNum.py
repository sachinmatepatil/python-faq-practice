lst = [1,2,4,45,234,345,12,33,4,234]

#Method 1: using inbuilt function

maxx=max(lst)
print(maxx)
minn=min(lst)
print(minn)

#Method 2 sort and then fetch first and last element
lst.sort()
print(lst)
print(lst[0],lst[-1])


def lar_num(lst):
    lar_num = 0

    for i in range(len(lst)):
        if lst[i] > lar_num:
            lar_num = lst[i]
    return lar_num


print(lar_num(lst))