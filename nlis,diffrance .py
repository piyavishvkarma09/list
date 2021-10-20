#Q: Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which numbers are not present in the second array.


list1 = [1,2,3,5,4,9,8,0]
list2 = [2,3,1,6,7]
i=0
a=[]
while i<len(list1):
    if list1[i] not in list2:
        a.append(list1[i])
    i=i+1
print(a)