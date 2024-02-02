students = ["Sam", "Alice", "Mona"]
subjects = ["Commerce", "Science", "Computer"]

student_subject_map = {student: subject for student, subject in zip(students, subjects)}

print("Output:", student_subject_map)