import json

with open("students.json", 'r') as f:
    students_data = json.load(f)

limited_data = [
    {"first_name": student["name"], "last_name": student["surname"], "student_id": student["student_id"]}
    for student in students_data
]

with open("limited.json", 'w') as file:
    json.dump(limited_data, file, indent=2)