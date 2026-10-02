# Student Grade Calculator

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
students = [
    ("Ravi", 95),
    ("Anu", 87),
    ("Rahul", 76),
    ("Priya", 64),
    ("Kiran", 52),
    ("Sneha", 38),
    ("Arjun", 105)
]
print("Student Grade Calculator")
for name, marks in students:
    grade = calculate_grade(marks)
    print(f"Student: {name} | Marks: {marks} | Grade: {grade}")
