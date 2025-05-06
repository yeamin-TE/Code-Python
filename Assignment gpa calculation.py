Assignments = float(input("Enter your assignment marks:"))
Tests = float(input("Enter your test score:"))
LabWorks = float(input("Enter your lab score:"))

finalscore = (Assignments * 0.10) + (Tests * 0.70) + (LabWorks * 0.20)

if finalscore >=90:
    grade = "A"
elif finalscore >=80:
    grade = "B"
elif finalscore >=70:
    grade = "C"
elif finalscore >=60:
    grade = "D"
elif finalscore >=50:
    grade = "E"
else:
    grade = "Failed"


print("Your final result/grade is:",grade)