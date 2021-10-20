#5. Write a Python program to count the number of strings where the string length is 2 or more
#  and the first and last character are same from a given list of 
# strings.Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
# mylist=["abc", "xyz"]
# print(len(mylist))


#6. Write a Python program to get a list, sorted in increasing order by
# the last element in each tuple from a given list of 
# non-empty tuples.= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# list1= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# list1= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# for i in range(len(list1)):
#       print(list1[-i-1])                    #######################

# 7. Write a Python program to remove duplicates from a list
# a= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
# b=[]
# c=[]
# i=0
# while i<len(a):
#     c1=0
#     j=0
#     while j<len(a):
#         if a[i]==(a[j]):
#             c.append(a[j])
#             c1=c1+1
#         j=j+1  
#     i=i+1    
#     k=0
#     while k<len(c):
#         if a[i] not in b:
#             b.append(a[i])
#             print((a[i]),"times",c1)
#         k=k+1
#     i=i+1


#q8 Write a Python program to check a list is empty or not.
# lis1 = []
# Enquiry=1
# if Enquiry in(lis1): 
#     print ("The list is not empty")
# else:
#     print("Empty List")


#q9 Write a Python program to clone or copy a list.
# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# numbers2=numbers.copy()
# print(numbers2)

#10 Write a Python program to find the list of words that are longer than n from a given list of words.
# str=input("enter strings : ")
# a=str.split(" ")
# b=[]
# n=int(input("enter value of n "))
# for i in a:
#     if (len(i)> n) :
#         b.append(i)
# print("list of words : ",b)

#56 Write a Python program to convert a string to a list.
# numbers="50","40", "23", "70", "56", "12", "5", "10", "7"
# print(list(numbers))



# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)
#q28
# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# index=0
# max=numbers[index]
# for m in numbers:
#     if m > max:
#         max=m
# print(max)
# numbers.remove(max)
# max=numbers[index]
# for m in numbers:
#     if m > max:
#         max=m
# print(max)

#q27
# number=[1,2,3,4,5,6,7]
# index=0
# smalest=number[index]
# for small in number:
#     if small <smalest:
#         smalest=small
# print(smalest)
# number.remove(smalest)
# smalest=number[index]
# for small in number:
#     if small <smalest:
#         smalest=small
# print(smalest)

#31Write a Python program to count the number of elements in a list within a specified range.
# number=[1,2,3,4,5,6,7]
# print(number[1:4])

#32. Write a Python program to check whether a list contains a sublist.
# number=[1,2,3,4,5,6,7]
# if 5 in number:
#     print("true")

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
# list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# list.pop(0)
# list.pop(4)
# list.pop()
# print(list)