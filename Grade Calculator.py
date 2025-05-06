marks = float(input("Enter your marks:"))

if marks >=80:
    grade = "A+"
elif marks >=70:
    grade = "A"
elif marks >=60:
    grade = "A-"
elif marks >=50:
    grade = "B"
elif marks >=50:
    grade = "C"
elif marks >=40:
    grade = "D"
else:
    grade = "Failed"

print("Your Result/grade is:",grade)