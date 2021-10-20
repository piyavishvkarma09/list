# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# index=0
# max=numbers[index]
# for i in numbers:
#     if i >max:
#         max=i
# print(max)

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
max=0
for i in numbers:
    if i >max:
        max=i
print(max)
numbers.remove(max)
max=0
for i in numbers:
    if i >max:
        max=i
print(max)



# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# max=0
# for i in numbers:
#     if i > max:
#         max=i
# print(max)
