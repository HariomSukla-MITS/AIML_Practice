name = input("Enter student name: ")

m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

total = m1 + m2 + m3
average = total / 3

if any(mark < 0 or mark > 100 for mark in [m1, m2, m3]):
    print("Invalid marks! Marks must be between 0 and 100.")
else:
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Student Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)