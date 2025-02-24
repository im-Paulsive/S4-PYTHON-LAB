import csv
import matplotlib.pyplot as plt

filename = "student.csv"

# Read student data
students = []
with open(filename, mode='r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        students.append(row)

# Update total marks
updated_students = []
for student in students:
    marks = list(map(int, student[2:]))  # Convert marks to integers
    total_marks = sum(marks)  # Compute total
    student.append(total_marks)  # Append total marks
    updated_students.append(student)
headers.append("Total Marks")

# Write updated data back to file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(updated_students)

# Search for a student
roll_no = input("Enter Roll No to search: ")
found_student = None
for student in updated_students:
    if student[0] == roll_no:
        found_student = student
        break

if found_student:
    print(f"Student Found: {found_student[1]} - Total Marks: {found_student[-1]}")
    
    # Display performance
    subjects = ["Subject1", "Subject2", "Subject3", "Subject4", "Subject5"]
    marks = list(map(int, found_student[2:7]))  # Extract marks
    
    plt.bar(subjects, marks, color='blue')
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title(f"Performance of {found_student[1]} (Roll No: {found_student[0]})")
    plt.ylim(0, 100)
    plt.show()
else:
    print("Student not found!")
