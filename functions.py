def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"


student_name = "Anjalee"
marks = [85, 92, 78, 88, 90]

average = calculate_average(marks)
grade = get_grade(average)

print("Student:", student_name)
print("Marks:", marks)
print("Average:", round(average, 2))
print("Grade:", grade)
