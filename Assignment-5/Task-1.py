# Dictionary containing student names and their marks
student_marks = {
    "alice": 85,
    "bob": 78,
    "charlie": 92,
    "david": 88
}

# Taking input from the user
name = input("Enter the student's name: ").strip().lower()

# Validation and retrieval
if name == "":
    print("Error: Student name cannot be empty.")
elif name in student_marks:
    print(f"Marks obtained by {name.capitalize()}: {student_marks[name]}")
else:
    print("Student not found in the records.")
