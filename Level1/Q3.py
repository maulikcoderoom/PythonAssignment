def cal_grade(marks):
    percentage = (sum(marks) / (len(marks) * 100)) * 100

    if percentage >= 90:
        return "Grade A"
    elif percentage >= 80:
        return "Grade B"
    elif percentage >= 70:
        return "Grade C"
    elif percentage >= 60:
        return "Grade D"
    elif percentage >= 40:
        return "Grade E"
    else:
        return "Grade F"

subjects = ["Physics", "Chemistry", "Biology", "Mathematics", "Computer"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter marks for {subject}: out of 100 "))
    marks.append(mark)

grade = cal_grade(marks)
print("Calculated Percentage is", round((sum(marks) / (len(marks) * 100)) * 100, 2))
print("Received Grade is", grade)
