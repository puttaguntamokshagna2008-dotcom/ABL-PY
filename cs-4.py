n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))
if n <= 0 or m <= 0:
    print("Students and subjects must be positive numbers.")
else:
    students = []
    for i in range(n):
        name = input(f"Enter student {i + 1} name: ")
        students.append(name)
    subjects = []
    for j in range(m):
        subject = input(f"Enter subject {j + 1} name: ")
        subjects.append(subject)
    marks = []
    for i in range(n):
        row = []
        print("\nEnter marks for", students[i])
        for j in range(m):
            mark = int(input(subjects[j] + ": "))
            while mark < 0 or mark > 100:
                print("Invalid marks! Enter marks between 0 and 100.")
                mark = int(input(subjects[j] + ": "))
            row.append(mark)
        marks.append(row)
    totals = []
    for i in range(n):
        total = sum(marks[i])
        average = total / m
        totals.append(total)
        print("Student:", students[i])
        print("Marks:", marks[i])
        print("Total:", total)
        print("Average:", round(average, 2))
    for j in range(m):
        subject_total = 0
        for i in range(n):
            subject_total += marks[i][j]
        subject_average = subject_total / n
        print(subjects[j], "Average:", round(subject_average, 2))
    highest_index = totals.index(max(totals))
    print("Highest-scoring student:", students[highest_index])
    print("Highest total marks:", totals[highest_index])
