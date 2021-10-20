a=[6,4,7,2,1,3]
new_list=[]
while a:
    min=a[0]
    for x in a:
        if x <min:
            min=x
    new_list.append(min)
    a.remove(min)
print(new_list)
