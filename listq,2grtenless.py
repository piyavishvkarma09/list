numbers=[50,40,23,70,56,12,5,10,7]
list_lenth=len(numbers)
greater_than20=0
less_than40=0
counter=0
while counter < list_lenth:
    number=numbers[counter]
    if number>20:
        greater_than20=greater_than20+1
    else:
        less_than40=less_than40+1
    counter=counter+1
    # print(counter)
print(greater_than20,"is grester than 20")
print(less_than40,"is less than 40") 