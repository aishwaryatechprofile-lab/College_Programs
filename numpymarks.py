
import numpy as np

n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    print("Enter marks of Student", i + 1)
    student_marks = []

    for j in range(5):
        mark = int(input("Enter marks for Subject " + str(j + 1) + ": "))
        student_marks.append(mark)

    marks.append(student_marks)

marks = np.array(marks)

for i in range(n):
    print("\nStudent", i + 1)
    print("Total Marks:", np.sum(marks[i]))
    print("Average Marks:", np.mean(marks[i]))
    print("Highest Marks:", np.max(marks[i]))
    print("Lowest Marks:", np.min(marks[i]))
