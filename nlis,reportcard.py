marks =[[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
i=0
length = len(marks)
index = 0
total_marks = 0
while index < len(marks):
    total_marks = marks[index] + total_marks
    index = index + 1
print ("Total Marks: "+str(total_marks))