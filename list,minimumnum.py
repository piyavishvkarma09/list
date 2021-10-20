# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# index=0
# minimum=numbers[index]
# for m in numbers:
#     if m <minimum:
#         minimum=m
# print(minimum) 

# a=[[2,3,4],[4,6,7],[6,5,8,9]]
# max=0
# for i in range (len(a)):
#     for j in a[i]:
#         if j >max:
#             max=j
#     print(max)

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
index=0
b=[]
minimum=numbers[index]
for m in (numbers):
    if m <minimum:
        minimum=m
        b.append(m)
        print(b)
        numbers.remove(m)
        i=0
        
