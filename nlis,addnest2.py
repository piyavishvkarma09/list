#Check your program for following nested lists as well 
#(bina code change kiye chalna chahiye, nahi toh aapne sahi se code nahi likha):

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
]
sum=0
for i in (marks):
    for j in i:
        sum=sum+j
print(sum)
