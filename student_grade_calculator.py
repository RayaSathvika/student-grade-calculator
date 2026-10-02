def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid Marks"
    elif marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


print("Student Grade Calculator")
print("-" * 30)

name = input("Enter student name: ")
marks = float(input("Enter marks: "))

grade = calculate_grade(marks)

print("\nResult")
print("-" * 30)
print("Student:", name)
print("Marks:", marks)
print("Grade:", grade)
