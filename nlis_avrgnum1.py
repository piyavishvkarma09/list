# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ]
# sum=0
# # avrage=0
# for i in (marks):
#     for j in i:
#         sum=sum+j
#         # avrage=sum/len(marks)      
# print(sum)
# # print(avrage)


# a=[1,2,3,4,[2,1],[2,1]]
# sum=0
# # avrage=0
# for i in a:
#     for j in a:
#         sum+=j
#     # avrage=sum/len(a)
# print(sum)
# # print(avrage)

# a=[1,2,3,4,[2,1],[2,1]]
# sum=0
# i=0
# while i<len(a):
#     b=a[i]
#     if type(b) is list:
#         j=0
#         for j in range (len(b)):        
#             sum+=b[j]
#     else:
#         sum=sum+a[i]
#     i+=1
# print(sum)



# a=[1,2,3,4,[2,1],[2,1]]
# sum=0
# i=0
# while i<len(a):
#     b=a[i]
#     if type(b) is list:
#         j=0
#         for j in range (len(b)):        
#             sum+=b[j]
#     else:
#         sum=sum+a[i]
#     i+=1
# print(sum)
# print(sum/len(a))

a=[1,2,[3,4,5,6],7,8,9,10]
i=0
sum=0
while i<len(a):
    # b=a[i]
    # print(type(a[i]))
    if type(a[i]) is list:
        # print(type(a[i]))
        j=0
        while j<len(a[i]):
            sum=sum+ a[i][j]
            # print(a[i][j])
            j+=1
    else:
        sum=sum+a[i]
    i+=1
print(sum)