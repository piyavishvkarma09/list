n=['n','i','t','i','n']
p_list=[]
i=1
while i<=len(n):
    p_list.append(n[-i])
    i=i+1
print(p_list)
if n==(p_list):
    print("palindrome")
else:
    print("not palindrome")


# a=int(input("enter a number: "))
# new_list=[]
# rem=0
# rev=0
# i=0
# n=a
# while n>0:
#     rem=n%10
#     rev=(rev*10)+rem
#     n=n//10
# if rev==a:
#     print("plindrome")
# else:
#     print("not a palindrome")